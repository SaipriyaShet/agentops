from fastapi import FastAPI
from app.agents.orchestrator import orchestrator
from app.schemas.query_schema import QueryRequest, QueryResponse
from app.dashboard.state import system_state
from fastapi.responses import Response

app = FastAPI(title="AgentOps API")

@app.post("/query", response_model=QueryResponse)
def query_agent(request: QueryRequest):
    return orchestrator(request.user_query)

@app.post("/simulate")
def simulate_agent():
    return orchestrator("simulate revenue behavior")

@app.get("/dashboard/state")
def dashboard_state():
    return system_state()


@app.get("/favicon.ico")
def favicon():
    return Response(status_code=204)
    
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "system": "AgentOps",
        "mode": "running"
    }
