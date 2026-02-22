from typing import List
from rapidfuzz import fuzz
from resumec.schemas.person import Project, Experience
from resumec.schemas.job import Job

def score_project(project: Project, keywords: List[str]) -> float:
    """Uses rapidfuzz to score a project against job keywords."""
    text = f"{project.name} {project.description} {' '.join(project.technologies)}"
    # Simple aggregated ratio
    score = sum(fuzz.partial_ratio(kw, text.lower()) for kw in keywords)
    return score / max(len(keywords), 1)

def score_experience(exp: Experience, keywords: List[str]) -> float:
    text = f"{exp.role} {exp.company} {' '.join(exp.bullets)}"
    score = sum(fuzz.partial_ratio(kw, text.lower()) for kw in keywords)
    return score / max(len(keywords), 1)
