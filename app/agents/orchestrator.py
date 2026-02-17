from app.agents.sql_agent import sql_agent
from app.agents.rag_agent import rag_agent
from app.agents.anomaly_agent import anomaly_agent
from app.agents.forecast_agent import forecast_agent
from app.agents.report_agent import report_agent
from app.agents.action_agent import action_agent

from app.config.system_mode import SYSTEM_MODE
from app.monitoring.logger import log_event

from app.memory.memory_store import save_event
from app.memory.memory_analyzer import analyze_memory

from app.intelligence.confidence_engine import (
    anomaly_confidence,
    forecast_confidence,
    action_confidence
)

from app.intelligence.feedback_loop import evaluate_feedback

from app.stability.rate_limiter import check_rate_limit
from app.stability.circuit_breaker import circuit_open
from app.stability.safe_mode import enforce_safe_mode
from app.actions.action_engine import execute_actions


def orchestrator(user_query: str):
    """
    Central brain of AgentOps system.
    Coordinates all agents, memory, confidence,
    feedback, and safety mechanisms.
    """

    reasoning_trace = []

    # ---------------------------
    # 0. Rate limiting
    # ---------------------------
    client_id = "local"  # later: request.client.host

    if not check_rate_limit(client_id):
        return {
            "error": "Rate limit exceeded",
            "message": "Too many requests, please slow down"
        }

    # ---------------------------
    # 1. Query received
    # ---------------------------
    log_event("User query received")
    reasoning_trace.append("User query received")

    # ---------------------------
    # 2. SQL Agent
    # ---------------------------
    sales_data = sql_agent(user_query)
    log_event("SQL agent executed")
    reasoning_trace.append("Sales data retrieved via SQL agent")

    # ---------------------------
    # 3. RAG Agent
    # ---------------------------
    knowledge = rag_agent(user_query)
    log_event("RAG agent executed")
    reasoning_trace.append("Context retrieved via RAG agent")

    # ---------------------------
    # 4. Anomaly Agent (adaptive)
    # ---------------------------
    anomaly_result = anomaly_agent(sales_data)
    log_event("Anomaly detection completed")
    reasoning_trace.append("Anomaly detection completed")

    # ---------------------------
    # 5. Forecast Agent
    # ---------------------------
    forecast_result = forecast_agent(sales_data)
    log_event("Forecast generated")
    reasoning_trace.append("Forecast generated")

    # ---------------------------
    # 6. Memory analysis
    # ---------------------------
    memory_analysis = analyze_memory(window_days=7)
    reasoning_trace.append(
        f"Memory analyzed (severity={memory_analysis['severity']})"
    )

    # ---------------------------
    # 7. Confidence scoring
    # ---------------------------
    anomaly_conf = anomaly_confidence(anomaly_result)
    forecast_conf = forecast_confidence(forecast_result, memory_analysis)
    action_conf = action_confidence(anomaly_conf, forecast_conf)

    reasoning_trace.append(
        f"Confidence computed "
        f"(anomaly={anomaly_conf}, forecast={forecast_conf})"
    )

    # ---------------------------
    # 8. Feedback loop
    # ---------------------------
    feedback = evaluate_feedback()

    if feedback.get("feedback_available"):
        reasoning_trace.append(
            f"Feedback evaluated (outcome={feedback['outcome']})"
        )
    else:
        reasoning_trace.append("Feedback skipped (insufficient data)")

    # ---------------------------
    # 9. Insight generation (LLM)
    # ---------------------------
    insight = report_agent(
        query=user_query,
        data=sales_data,
        knowledge=knowledge,
        reasoning=reasoning_trace
    )

    # ---------------------------
    # 10. Action decision (system mode)
    # ---------------------------
    if SYSTEM_MODE == "observe":
        actions = []
        reasoning_trace.append("System mode: OBSERVE")

    elif SYSTEM_MODE == "advise":
        actions = action_agent(anomaly_result, forecast_result)
        reasoning_trace.append("System mode: ADVISE")

    else:
        actions = []
        reasoning_trace.append("System mode: ACT (disabled)")

    # ---------------------------
    # 11. Stability enforcement
    # ---------------------------
    breaker_open = circuit_open()
    actions = enforce_safe_mode(actions, breaker_open)

    if breaker_open:
        reasoning_trace.append(
            "Circuit breaker open → switched to safe observe mode"
        )
        # ---------------------------
    # 11.5 Execute actions
    # ---------------------------
    executed_actions = execute_actions(
        actions=actions,
        confidence=action_conf
    )

    if executed_actions:
        reasoning_trace.append(
            f"Executed actions: {executed_actions}"
        )
    else:
        reasoning_trace.append(
            "No actions executed (safety or mode constraints)"
        )

    # ---------------------------
    # 12. Persist memory
    # ---------------------------
    save_event({
        "query": user_query,
        "anomaly": anomaly_result,
        "forecast": forecast_result,
        "actions": actions
    })

    # ---------------------------
    # 13. Final response
    # ---------------------------
    return {
        "agent": "AgentOps Orchestrator",
        "system_mode": SYSTEM_MODE,
        "reasoning_trace": reasoning_trace,
        "anomaly_analysis": anomaly_result,
        "forecast": forecast_result,
        "memory_analysis": memory_analysis,
        "confidence": {
            "anomaly_confidence": anomaly_conf,
            "forecast_confidence": forecast_conf,
            "action_confidence": action_conf
        },
        "feedback": feedback,
        "recommended_actions": actions,
        "generated_insight": insight,
        "executed_actions": executed_actions,
    }
