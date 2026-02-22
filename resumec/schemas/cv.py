from typing import List
from pydantic import BaseModel
from .person import Contact, Education, SkillCategory, Experience, Project


class CV(BaseModel):
    """The final compiled CV schema ready for template rendering."""
    name: str
    target_role: str
    summary: str
    contact: Contact
    education: List[Education]
    skills: List[SkillCategory]
    experience: List[Experience]
    projects: List[Project]
