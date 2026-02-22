import trafilatura

def fetch_job_posting(url: str) -> str:
    """Fetches job description text from a given URL."""
    downloaded = trafilatura.fetch_url(url)
    if not downloaded:
        return ""
    text = trafilatura.extract(downloaded)
    return text or ""
