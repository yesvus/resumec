from typing import List
from resumec.schemas.person import Project

def classify_project(project: Project, keywords: List[str]) -> str:
    """Classifies a project into a category based on matched keywords."""
    project_text = (project.description + " " + " ".join(project.technologies)).lower()
    
    match_count = sum(1 for kw in keywords if kw in project_text)
    
    if match_count > 3:
        return "Highly Relevant"
    elif match_count > 0:
        return "Relevant"
    return "Other"
