import os

def load_raw_cv(filepath: str) -> str:
    """Reads the raw CV markdown file from disk."""
    if not os.path.exists(filepath):
        return ""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()
