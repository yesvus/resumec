import os
from resumec.pipeline.ingest.job_fetcher import fetch_job_posting
from resumec.pipeline.ingest.repo_crawler import crawl_active_repos
from resumec.pipeline.ingest.rawcv_loader import load_raw_cv

from resumec.pipeline.normalize.job_parser import parse_job
from resumec.pipeline.normalize.person_parser import parse_person
from resumec.pipeline.normalize.repo_parser import parse_repos

from resumec.pipeline.enrich.extract_keywords import extract_keywords
from resumec.pipeline.enrich.classify_project import classify_project

from resumec.pipeline.match.selector import select_top_projects, select_top_experience
from resumec.pipeline.generate.rewrite_cv import rewrite_summary
from resumec.pipeline.validate.repair import process_bullets
from resumec.schemas.cv import CV

from resumec.pipeline.render.markdown_renderer import render_markdown
from resumec.pipeline.persist.save_cv import save_markdown_cv

def compile_cv(job_url: str):
    """The main pipeline orchestrator."""
    print(f"Starting CV compilation for {job_url}...")
    
    # 1. Load Raw CV (assume it's in the project root for testing)
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    raw_cv_text = load_raw_cv(os.path.join(project_root, "data", "raw_cv.md"))
    
    # 2. Fetch Job Posting
    print("Fetching job description...")
    job_text = fetch_job_posting(job_url)
    
    # 3. Crawl Github (Mock mapped to 'janedoe')
    print("Crawling GitHub repos...")
    raw_repos = crawl_active_repos("janedoe")
    
    # 4. Normalize
    print("Normalizing data to Pydantic schemas...")
    person = parse_person(raw_cv_text)
    job = parse_job(job_url, job_text)
    repos = parse_repos(raw_repos)
    
    # 5. Extract Keywords
    print("Extracting keywords...")
    keywords = extract_keywords(job)
    
    # 6. Score and Select
    print("Selecting best matching projects and experience...")
    top_projects = select_top_projects(person.projects, keywords, top_n=3)
    top_experience = select_top_experience(person.experience, keywords, top_n=2)
    
    # 7 & 8. Generate and Validate (Repair loop mapping)
    print("Rewriting and validating to match job posting...")
    final_summary = rewrite_summary(person.summary, keywords)
    
    for exp in top_experience:
        exp.bullets = process_bullets(exp.bullets, keywords)
        
    for proj in top_projects:
        proj.bullets = process_bullets(proj.bullets, keywords)
        
    # Build complete CV object
    final_cv = CV(
        name=person.name,
        target_role=job.title,
        summary=final_summary,
        contact=person.contact,
        education=person.education,
        skills=person.skills,
        experience=top_experience,
        projects=top_projects
    )
    
    # 9. Render Markdown
    print("Rendering markdown template...")
    markdown_output = render_markdown(final_cv)
    
    # 10. Persist
    print("Saving final CV...")
    saved_path = save_markdown_cv(markdown_output, job.title, job.company)
    print(f"Success! CV saved to: {saved_path}")
