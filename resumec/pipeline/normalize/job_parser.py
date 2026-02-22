from resumec.schemas.job import Job

def parse_job(url: str, text: str) -> Job:
    """Extracts job details from raw text (Mocked for simplicity)."""
    # In a real app, this might use NLP or light regex heuristics
    # to extract job title, company, requirements, etc.
    return Job(
        title="Software Engineer",
        company="Tech Corp",
        url=url,
        description=text[:200] + "..." if len(text) > 200 else text,
        requirements=["Python", "FastAPI", "PostgreSQL"],
        responsibilities=["Build scalable APIs", "Maintain pipelines"]
    )
