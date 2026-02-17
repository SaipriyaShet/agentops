def action_agent(anomaly_result, forecast_result):
    actions = []

    if anomaly_result.get("anomaly"):
        actions.append("Investigate recent changes in traffic or conversion funnel")
        actions.append("Review active marketing campaigns")

    if forecast_result.get("forecast_next_period") is not None:
        actions.append("Prepare resources based on forecasted demand")

    if not actions:
        actions.append("Maintain current strategy and monitor performance")

    return actions
