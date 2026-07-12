from pydantic import BaseModel
from typing import List


class AgentRequest(BaseModel):
    request: str


class AgentResponse(BaseModel):
    request: str
    plan: List[str]
    status: str
    document: str
    output: str