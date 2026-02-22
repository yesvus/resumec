from typing import List, Optional
from pydantic import BaseModel, Field


class Repo(BaseModel):
    name: str
    url: str
    description: Optional[str] = None
    language: Optional[str] = None
    stars: int = 0
    topics: List[str] = Field(default_factory=list)
