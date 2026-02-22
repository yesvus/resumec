from typing import List, Tuple
from resumec.schemas.person import Project, Experience
from resumec.pipeline.match.scorer import score_project, score_experience

def select_top_projects(projects: List[Project], keywords: List[str], top_n: int = 3) -> List[Project]:
    """Selects the top N projects based on keyword scoring."""
    scored = [(p, score_project(p, keywords)) for p in projects]
    scored.sort(key=lambda x: x[1], reverse=True)
    return [p for p, _ in scored][:top_n]

def select_top_experience(experiences: List[Experience], keywords: List[str], top_n: int = 3) -> List[Experience]:
    """Selects the top N experiences based on keyword scoring."""
    scored = [(e, score_experience(e, keywords)) for e in experiences]
    scored.sort(key=lambda x: x[1], reverse=True)
    return [e for e, _ in scored][:top_n]
