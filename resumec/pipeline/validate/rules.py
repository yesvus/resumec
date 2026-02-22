import re
from typing import List, Tuple

def validate_length(bullet: str) -> bool:
    return len(bullet) <= 140

def validate_no_first_person(bullet: str) -> bool:
    pattern = r'\b(I|me|my|mine|we|us|our|ours)\b'
    return not bool(re.search(pattern, bullet, re.IGNORECASE))

def validate_action_verb(bullet: str) -> bool:
    # A simple proxy: ensure the first word is alphabetical and long enough,
    # or implement an NLP pos_tagger. We will do a simple check.
    words = bullet.split()
    if not words: return False
    return words[0].isalpha()

def validate_bullet(bullet: str) -> Tuple[bool, List[str]]:
    """Runs all validation rules returning a boolean pass and list of errors."""
    errors = []
    if not validate_length(bullet):
        errors.append(f"Length > 140 chars: {len(bullet)}")
    if not validate_no_first_person(bullet):
        errors.append("Contains first-person pronouns.")
    if not validate_action_verb(bullet):
        errors.append("Does not start with an apparent action verb.")
    
    return len(errors) == 0, errors
