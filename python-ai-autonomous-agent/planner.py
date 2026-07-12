import json

from config import model


def create_plan(request: str) -> list[str]:
    """
    Generate an autonomous execution plan.
    """

    prompt = f"""
You are an Autonomous AI Planner.

User Request:
{request}

Create between 5 and 7 high-level execution steps.

Rules:
- Understand the request.
- Break it into logical tasks.
- Keep steps concise.
- Merge related activities.
- Return ONLY valid JSON.

Example:

{{
  "tasks": [
    "Analyze requirements",
    "Define objectives",
    "Identify key features",
    "Create implementation strategy",
    "Estimate timeline and budget",
    "Generate final business proposal"
  ]
}}
"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    # Remove markdown if Gemini returns it
    text = text.replace("```json", "").replace("```", "").strip()

    try:
        data = json.loads(text)
        tasks = data.get("tasks", [])
    except Exception:
        tasks = []

        for line in text.split("\n"):
            line = line.strip()

            if not line:
                continue

            if "." in line and line.split(".")[0].isdigit():
                line = line.split(".", 1)[1].strip()

            line = (
                line.replace("-", "")
                    .replace("*", "")
                    .replace("•", "")
                    .strip()
            )

            if line:
                tasks.append(line)

    print("\n========== Execution Plan ==========")

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

    print("====================================\n")

    return tasks