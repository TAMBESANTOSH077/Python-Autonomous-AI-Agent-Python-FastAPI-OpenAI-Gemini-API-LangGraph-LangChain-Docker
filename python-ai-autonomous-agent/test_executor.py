from planner import create_plan
from executor import execute_plan

request = "Create a business proposal for an AI-powered hospital chatbot."

plan = create_plan(request)

print("\nExecution Plan")
print("-" * 40)

for i, task in enumerate(plan, start=1):
    print(f"{i}. {task}")

print("\nGenerating document...\n")

content = execute_plan(request, plan)

print(content)