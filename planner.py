"""Simple rule-based prioritization and study scheduling."""
from datetime import date


def priority_score(task):
    days_left = (date.fromisoformat(task['deadline']) - date.today()).days
    urgency = 50 if days_left < 0 else 30 if days_left == 0 else max(0, 20 - days_left * 2)
    return urgency + task['importance'] * 5 + task['difficulty'] * 3


def ranked_tasks(tasks):
    pending = [task for task in tasks if not task['completed']]
    return sorted(pending, key=lambda task: (-priority_score(task), task['deadline'], task['id']))


def create_schedule(tasks, available_minutes):
    """Allocate minutes in priority order, up to each task's remaining estimate."""
    schedule = []
    remaining = available_minutes
    for task in ranked_tasks(tasks):
        if remaining <= 0:
            break
        minutes = min(remaining, task['minutes'])
        if minutes > 0:
            schedule.append((task, minutes))
            remaining -= minutes
    return schedule
