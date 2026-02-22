from typing import List
from resumec.schemas.job import Job

def extract_keywords(job: Job) -> List[str]:
    """
    Extracts essential keywords from the job description and requirements.
    In a real system, this could use spaCy or an LLM call to extract entities.
    Here we do a simple mock based on the requirements list.
    """
    keywords = set()
    for req in job.requirements:
        # Simplistic split
        for word in req.replace(",", "").split():
            if len(word) > 2:
                keywords.add(word.lower())
    return list(keywords)
