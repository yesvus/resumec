from typing import List, Optional
from pydantic import BaseModel, Field


class Job(BaseModel):
    title: str
    company: str
    url: str
    description: str
    requirements: List[str] = Field(default_factory=list)
    responsibilities: List[str] = Field(default_factory=list)
