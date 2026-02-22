import os
from datetime import datetime

def save_markdown_cv(content: str, role: str, company: str) -> str:
    """Saves the completely rendered CV into the correct directory."""
    date_str = datetime.now().strftime("%Y-%m-%d")
    sanitized_role = "".join([c if c.isalnum() else "_" for c in role])
    sanitized_company = "".join([c if c.isalnum() else "_" for c in company])
    
    filename = f"{date_str}_{sanitized_role}_{sanitized_company}.md"
    # __file__ is dev/resumec/resumec/pipeline/persist/save_cv.py
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    cvs_dir = os.path.join(project_root, "cvs")
    
    os.makedirs(cvs_dir, exist_ok=True)
    filepath = os.path.join(cvs_dir, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
    return filepath
