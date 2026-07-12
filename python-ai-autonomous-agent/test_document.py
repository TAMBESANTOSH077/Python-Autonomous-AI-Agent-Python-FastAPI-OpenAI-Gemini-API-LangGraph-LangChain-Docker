from planner import create_plan
from executor import execute_plan
from document import generate_document

request = "Create a business proposal for an AI-powered hospital chatbot."

plan = create_plan(request)

from reflection import review_document

content = execute_plan(request, plan)

improved_content = review_document(content)

file_path = generate_document(
    request,
    improved_content
)

print(file_path)