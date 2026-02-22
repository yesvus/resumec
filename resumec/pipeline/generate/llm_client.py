import os
import instructor
from openai import OpenAI
from pydantic import BaseModel
from resumec.config import settings

# For this MVP and the mock requirement, we can intercept calls 
# or use a mock client.
class MockLLMClient:
    def chat_completion(self, response_model: type[BaseModel], messages: list) -> BaseModel:
        """Returns mock Pydantic objects instead of calling API."""
        # Simple heuristic to return mock data based on the request's model
        model_name = response_model.__name__
        if model_name == "RewrittenBullets":
            return response_model(bullets=["Successfully built robust APIs using Python.", "Improved performance of the database by 20% using PostgreSQL optimizations."])
        if model_name == "RewrittenSummary":
            return response_model(summary="A highly skilled software engineer experienced in Python, ready to deliver impactful pipelines.")
        # Fallback empty
        return response_model()

# Setup client properly if API key exists, otherwise mock
if settings.openai_api_key and settings.openai_api_key != "MOCK":
    client = instructor.from_openai(OpenAI(api_key=settings.openai_api_key))
else:
    client = MockLLMClient()

def get_client():
    return client
