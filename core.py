# core.py — основна логіка (після рефакторингу)

from validator import is_valid_event

events = []

def process_event(event):
    """Обробляє подію після валідації."""
    if not is_valid_event(event):
        return None
    result = {
        "id": len(events) + 1,
        "type": event["type"],
        "data": event["data"],
        "processed": True
    }
    events.append(result)
    return result

def get_all_events():
    return events

def clear_events():
    events.clear()