# validator.py — валідація подій

ALLOWED_TYPES = ["click", "login", "logout", "error", "info"]

def is_valid_event(event):
    """Перевіряє чи подія коректна."""
    if not isinstance(event, dict):
        return False
    if "type" not in event or "data" not in event:
        return False
    if event["type"] not in ALLOWED_TYPES:
        return False
    if not event["data"]:
        return False
    return True

def filter_valid(events):
    """Повертає тільки валідні події."""
    return [e for e in events if is_valid_event(e)]