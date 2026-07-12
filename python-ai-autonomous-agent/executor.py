import google.generativeai as genai
from config import model
from config import GEMINI_API_KEY
from prompts import SYSTEM_PROMPT

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction=SYSTEM_PROMPT
)


def execute_plan(request: str, plan: list[str]) -> str:
    """
    Execute the complete plan in a single LLM call
    and generate one professional business document.
    """

    execution_plan = "\n".join(
        [f"{i+1}. {task}" for i, task in enumerate(plan)]
    )

    prompt = f"""
You are a Professional Business Analyst and Technical Writer.

User Request:
{request}

Execution Plan:
{execution_plan}

Your task is to execute the complete plan and generate one professional business document.

Requirements:
- Follow every step in the execution plan.
- Use headings and subheadings.
- Write detailed content.
- Make reasonable assumptions if information is missing.
- Do NOT use placeholders like [Your Name] or [Company].
- Do NOT write a letter or email.
- Produce a polished business document.

Return only the final document.
"""

    response = model.generate_content(prompt)

    return response.text.strip()