from typing import List, Dict, Any

def crawl_active_repos(username: str) -> List[Dict[str, Any]]:
    """Mocks crawling of GitHub repositories for a user."""
    # In a real app, this would use httpx and github API
    return [
        {
            "name": "resumec",
            "url": f"https://github.xyz/{username}/resumec",
            "description": "Deterministic CV compiler built with Python",
            "language": "Python",
            "stars": 42,
            "topics": ["cli", "python", "jinja2", "resume-builder"]
        },
        {
            "name": "legacy-crud-app",
            "url": f"https://github.xyz/{username}/legacy-crud-app",
            "description": "A boring CRUD application in Java",
            "language": "Java",
            "stars": 1,
            "topics": ["java", "spring-boot"]
        }
    ]
