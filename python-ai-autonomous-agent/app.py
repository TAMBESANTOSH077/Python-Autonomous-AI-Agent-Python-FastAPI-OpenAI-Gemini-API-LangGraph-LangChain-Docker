from fastapi import FastAPI, HTTPException

from models import AgentRequest, AgentResponse
from planner import create_plan
from executor import execute_plan
from reflection import review_document
from document import generate_document

app = FastAPI(
    title="Autonomous AI Agent",
    version="1.0.0",
    description="Autonomous AI Agent for Business Document Generation"
)


@app.get("/")
def home():
    return {
        "status": "success",
        "message": "Autonomous AI Agent API is running."
    }


@app.post("/agent", response_model=AgentResponse)
def run_agent(data: AgentRequest):

    try:

        # Validate request
        if not data.request.strip():
            raise HTTPException(
                status_code=400,
                detail="Request cannot be empty."
            )

        # Step 1: Planning
        plan = create_plan(data.request)

        # Step 2: Execution
        content = execute_plan(data.request, plan)

        # Step 3: Reflection
        improved_content = review_document(content)

        # Step 4: Generate Word Document
        document_path = generate_document(
            data.request,
            improved_content
        )

        return AgentResponse(
            request=data.request,
            plan=plan,
            status="completed",
            document=document_path,
            output=improved_content
        )

    except HTTPException:
        raise

    except Exception as e:
        print("ERROR:", e)

        raise HTTPException(
            status_code=500,
            detail=f"Agent execution failed: {str(e)}"
        )