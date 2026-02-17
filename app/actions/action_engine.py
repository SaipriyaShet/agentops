from app.monitoring.logger import log_event
from app.config.system_mode import SYSTEM_MODE

CONFIDENCE_THRESHOLD = 0.7

def execute_actions(actions, confidence):
    """
    Execute real-world actions safely.
    """

    executed = []

    if SYSTEM_MODE != "act":
        log_event("System not in ACT mode — actions skipped")
        return executed

    if confidence < CONFIDENCE_THRESHOLD:
        log_event("Low confidence — actions suppressed")
        return executed

    for action in actions:
        if action == "log":
            log_action()
            executed.append("log")

        elif action == "webhook":
            webhook_action()
            executed.append("webhook")

        elif action == "email":
            email_action()
            executed.append("email")

    return executed


def log_action():
    log_event("ACTION: Logged anomaly to audit system")


def webhook_action():
    # placeholder for real integration
    log_event("ACTION: Webhook triggered (mock)")


def email_action():
    # placeholder for real email
    log_event("ACTION: Email notification sent (mock)")
