from app.memory.memory_store import load_memory

def evaluate_feedback():
    """
    Evaluates past decisions to see if actions led to improvement.
    """

    memory = load_memory()

    if len(memory) < 3:
        return {
            "feedback_available": False,
            "reason": "Insufficient historical data"
        }

    # Compare last two events
    prev = memory[-2]
    curr = memory[-1]

    prev_rev = prev.get("forecast", {}).get("forecast_next_period")
    curr_rev = curr.get("forecast", {}).get("forecast_next_period")

    if prev_rev is None or curr_rev is None:
        return {
            "feedback_available": False,
            "reason": "Missing forecast data"
        }

    if curr_rev > prev_rev:
        outcome = "positive"
    elif curr_rev < prev_rev:
        outcome = "negative"
    else:
        outcome = "neutral"

    return {
        "feedback_available": True,
        "outcome": outcome,
        "prev_forecast": prev_rev,
        "current_forecast": curr_rev
    }
