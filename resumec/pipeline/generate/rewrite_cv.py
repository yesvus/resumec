from typing import List, Optional
from pydantic import BaseModel
from resumec.pipeline.generate.llm_client import get_client
from resumec.pipeline.generate.prompts import SYSTEM_REWRITE_BULLETS, SYSTEM_REWRITE_SUMMARY

class RewrittenBullets(BaseModel):
    bullets: List[str]

class RewrittenSummary(BaseModel):
    summary: str

def rewrite_bullets(original_bullets: List[str], keywords: List[str], feedback: Optional[str] = None) -> List[str]:
    """Calls LLM to rewrite bullet points using instructor to enforce JSON schema."""
    client = get_client()
    user_content = f"Original Bullets:\n{chr(10).join(original_bullets)}\n\nKeywords: {', '.join(keywords)}"
    if feedback:
        user_content += f"\n\nFEEDBACK TO FIX: {feedback}"
        
    messages = [
        {"role": "system", "content": SYSTEM_REWRITE_BULLETS},
        {"role": "user", "content": user_content}
    ]
    
    # In a mock setup, this returns the mock object directly
    if hasattr(client, 'chat_completion'):
        resp = client.chat_completion(response_model=RewrittenBullets, messages=messages)
    else:
        # Instructor real client
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            response_model=RewrittenBullets,
            messages=messages,
            max_retries=3
        )
    return resp.bullets

def rewrite_summary(original_summary: str, keywords: List[str]) -> str:
    client = get_client()
    user_content = f"Original Summary: {original_summary}\n\nKeywords: {', '.join(keywords)}"
    
    messages = [
        {"role": "system", "content": SYSTEM_REWRITE_SUMMARY},
        {"role": "user", "content": user_content}
    ]
    
    if hasattr(client, 'chat_completion'):
        resp = client.chat_completion(response_model=RewrittenSummary, messages=messages)
    else:
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            response_model=RewrittenSummary,
            messages=messages,
            max_retries=3
        )
    return resp.summary
