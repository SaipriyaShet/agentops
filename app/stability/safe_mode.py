def enforce_safe_mode(actions, circuit_open: bool):
    if circuit_open:
        return []
    return actions
