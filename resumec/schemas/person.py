from typing import List, Optional
from pydantic import BaseModel, Field


class Contact(BaseModel):
    email: str
    phone: Optional[str] = None
    location: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None
    website: Optional[str] = None


class Education(BaseModel):
    institution: str
    degree: str
    start_date: str
    end_date: Optional[str] = None
    gpa: Optional[float] = None
    details: List[str] = Field(default_factory=list)


class SkillCategory(BaseModel):
    name: str # e.g., "Languages", "Frameworks"
    skills: List[str]


class Experience(BaseModel):
    company: str
    role: str
    start_date: str
    end_date: Optional[str] = None
    location: Optional[str] = None
    bullets: List[str]


class Project(BaseModel):
    name: str
    description: str
    technologies: List[str] = Field(default_factory=list)
    link: Optional[str] = None
    bullets: List[str] = Field(default_factory=list)


class Person(BaseModel):
    name: str
    summary: str
    contact: Contact
    education: List[Education]
    skills: List[SkillCategory]
    experience: List[Experience]
    projects: List[Project]
