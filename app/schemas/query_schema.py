from pydantic import BaseModel

class QueryRequest(BaseModel):
    user_query: str

class QueryResponse(BaseModel):
    agent: str
    reasoning_trace: list
    anomaly_analysis: dict
    forecast: dict
    recommended_actions: list
    generated_insight: str
