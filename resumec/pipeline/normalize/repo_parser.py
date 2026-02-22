from typing import List, Dict, Any
from resumec.schemas.repo import Repo

def parse_repos(raw_repos: List[Dict[str, Any]]) -> List[Repo]:
    """Converts a raw list of repo dictionaries into Pydantic models."""
    repos = []
    for r in raw_repos:
        repos.append(Repo(
            name=r.get("name", ""),
            url=r.get("url", ""),
            description=r.get("description"),
            language=r.get("language"),
            stars=r.get("stars", 0),
            topics=r.get("topics", [])
        ))
    return repos
