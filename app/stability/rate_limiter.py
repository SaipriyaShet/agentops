import time
from collections import defaultdict

REQUEST_LIMIT = 20        # max requests
WINDOW_SECONDS = 60       # per minute

_requests = defaultdict(list)

def check_rate_limit(client_id: str):
    now = time.time()
    window_start = now - WINDOW_SECONDS

    _requests[client_id] = [
        t for t in _requests[client_id] if t > window_start
    ]

    if len(_requests[client_id]) >= REQUEST_LIMIT:
        return False

    _requests[client_id].append(now)
    return True
