"""Read and write study tasks as JSON."""
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name('tasks.json')


def load_tasks():
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open('r', encoding='utf-8') as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print('Warning: Could not read tasks.json. Starting with an empty list.')
        return []


def save_tasks(tasks):
    with DATA_FILE.open('w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=2)
