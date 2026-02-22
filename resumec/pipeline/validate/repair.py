from typing import List
from resumec.pipeline.generate.rewrite_cv import rewrite_bullets
from resumec.pipeline.validate.rules import validate_bullet

def process_bullets(bullets: List[str], keywords: List[str], max_loops: int = 3) -> List[str]:
    """
    Repair loop applying rules, feedback, and re-calling LLM if invalid.
    """
    current_bullets = rewrite_bullets(bullets, keywords)
    
    for attempt in range(max_loops):
        all_passed = True
        all_feedback = []
        for b in current_bullets:
            passed, errors = validate_bullet(b)
            if not passed:
                all_passed = False
                all_feedback.append(f"Bullet '{b}' failed: {', '.join(errors)}")
        
        if all_passed:
            return current_bullets
            
        # Give feedback to LLM for repair
        feedback_text = "\n".join(all_feedback)
        current_bullets = rewrite_bullets(bullets, keywords, feedback=feedback_text)
        
    # If it fails all loops, just return the best we have (or fallback)
    # The requirement is deterministic so we might just truncate/strip on worst case
    return current_bullets
