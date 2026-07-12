import google.generativeai as genai

from config import GEMINI_API_KEY
from prompts import SYSTEM_PROMPT 
from config import model


genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction=SYSTEM_PROMPT
)


def review_document(content: str) -> str:
    """
    Review and improve the generated document.
    """

    prompt = f"""
You are a senior Business Consultant.

Review the following document.

Check for:
- Grammar mistakes
- Missing information
- Professional tone
- Logical flow
- Clarity
- Completeness

Improve the document if needed.

Return ONLY the improved document.

Document:

{content}
"""

    response = model.generate_content(prompt)

    return response.text.strip()