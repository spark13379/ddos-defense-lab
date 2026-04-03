import time
from collections import defaultdict
from .config import RATE_LIMIT, BLOCK_TIME

requests_log = defaultdict(list)
blocked_ips = {}

def is_blocked(ip):
    if ip in blocked_ips:
        if time.time() < blocked_ips[ip]:
            return True
        else:
            del blocked_ips[ip]
    return False

def check_rate_limit(ip):
    now = time.time()

    if is_blocked(ip):
        return False

    # mantém apenas últimos 60 segundos
    requests_log[ip] = [t for t in requests_log[ip] if now - t < 60]

    if len(requests_log[ip]) >= RATE_LIMIT:
        blocked_ips[ip] = now + BLOCK_TIME
        return False

    requests_log[ip].append(now)
    return True