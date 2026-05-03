from django.conf import settings
from google import genai


def get_ai_response(message):
    if not settings.GEMINI_API_KEY:
        return (
            "The AI service is not configured yet. Add GEMINI_API_KEY to your "
            ".env file and restart the server."
        )

    client = genai.Client(api_key=settings.GEMINI_API_KEY)
    response = client.models.generate_content(
        model=settings.GEMINI_MODEL,
        contents=message,
    )
    return response.text or "I could not generate a response. Please try again."
