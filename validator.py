# validator.py — після виправлення бага

ALLOWED_TYPES = ["click", "login", "logout", "error", "info"]

def is_valid_event(event):
    if not isinstance(event, dict):
        return False
    if "type" not in event or "data" not in event:
        return False
    if event["type"] not in ALLOWED_TYPES:
        return False  # "unknown" тепер теж відхиляється
    if not str(event["data"]).strip():
        return False
    return True

def filter_valid(events):
    return [e for e in events if is_valid_event(e)]