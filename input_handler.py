# input_handler.py — обробка вхідних даних

def parse_input(raw_input):
    """Перетворює рядок у словник події."""
    parts = raw_input.strip().split(":")
    if len(parts) < 2:
        return {"type": "unknown", "data": raw_input}
    return {
        "type": parts[0].strip(),
        "data": parts[1].strip()
    }

def read_events_from_list(event_list):
    """Читає список рядків і повертає список подій."""
    return [parse_input(line) for line in event_list if line.strip()]