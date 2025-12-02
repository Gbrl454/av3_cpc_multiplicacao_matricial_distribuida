import json
import datetime
import os

def default_serializer(obj):
    if isinstance(obj, (datetime.datetime, datetime.date, datetime.time)):
        return obj.isoformat()

    if isinstance(obj, datetime.timedelta):
        return obj.total_seconds()

    if hasattr(obj, "__dict__"):
        return obj.__dict__

    return str(obj)


def save_json(obj, path_file):
    os.makedirs(os.path.dirname(path_file), exist_ok=True)

    with open(path_file, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=4, ensure_ascii=False, default=default_serializer)
