from planner import create_plan
from executor import execute_plan
from reflection import review_document

request = "Create a business proposal for an AI-powered hospital chatbot."

plan = create_plan(request)

content = execute_plan(request, plan)

improved_content = review_document(content)

print(improved_content)