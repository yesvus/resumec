import os
from jinja2 import Environment, FileSystemLoader
from resumec.schemas.cv import CV

def render_markdown(cv: CV, template_name: str = "swe.md.jinja") -> str:
    """Renders the final CV model into markdown using Jinja2."""
    template_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "templates")
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_name)
    
    # We pass the pydantic model as dict for easy access
    return template.render(cv=cv.model_dump())
