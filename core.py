# core.py — основна логіка обробки подій

events = []

def process_event(event):
    """Обробляє подію і додає до списку."""
    result = {
        "id": len(events) + 1,
        "type": event.get("type", "unknown"),
        "data": event.get("data", ""),
        "processed": True
    }
    events.append(result)
    return result

def get_all_events():
    """Повертає всі оброблені події."""
    return events

def clear_events():
    """Очищає список подій."""
    events.clear()