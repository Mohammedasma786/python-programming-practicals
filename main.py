"""SmartStudy AI: a beginner-friendly terminal study planner."""
from datetime import date
from planner import create_schedule, ranked_tasks
from storage import load_tasks, save_tasks


def read_number(prompt, minimum=1, maximum=None):
    while True:
        try:
            value = int(input(prompt))
            if value >= minimum and (maximum is None or value <= maximum):
                return value
        except ValueError:
            pass
        print('Please enter a valid whole number.')


def read_date():
    while True:
        value = input('Deadline (YYYY-MM-DD): ').strip()
        try:
            date.fromisoformat(value)
            return value
        except ValueError:
            print('Use a valid date such as 2026-12-15.')


def add_task(tasks):
    title = input('Task name: ').strip()
    if not title:
        print('Task name cannot be empty.')
        return
    subject = input('Subject: ').strip() or 'General'
    deadline = read_date()
    difficulty = read_number('Difficulty (1 easy - 5 hard): ', 1, 5)
    importance = read_number('Importance (1 low - 5 high): ', 1, 5)
    minutes = read_number('Estimated study time in minutes: ')
    task = {
        'id': max((task['id'] for task in tasks), default=0) + 1,
        'title': title,
        'subject': subject,
        'deadline': deadline,
        'difficulty': difficulty,
        'importance': importance,
        'minutes': minutes,
        'completed': False,
    }
    tasks.append(task)
    save_tasks(tasks)
    print('Task added successfully!')


def view_tasks(tasks):
    if not tasks:
        print('No tasks yet. Add your first task!')
        return
    for task in sorted(tasks, key=lambda item: item['id']):
        status = 'Done' if task['completed'] else 'Pending'
        print(f"#{task['id']} | {task['subject']} | {task['title']} | "
              f"Due: {task['deadline']} | {task['minutes']} min | {status}")


def mark_complete(tasks):
    task_id = read_number('Task ID to complete: ')
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            save_tasks(tasks)
            print('Task marked complete!')
            return
    print('Task ID not found.')


def delete_task(tasks):
    task_id = read_number('Task ID to delete: ')
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print('Task deleted!')
            return
    print('Task ID not found.')


def show_schedule(tasks):
    minutes = read_number('How many minutes can you study today? ')
    schedule = create_schedule(tasks, minutes)
    if not schedule:
        print('No pending tasks to schedule.')
        return
    print('\nYour smart study schedule:')
    for task, allocated in schedule:
        print(f"- {task['subject']}: {task['title']} — {allocated} min "
              f"(due {task['deadline']})")
    print(f'Total scheduled: {sum(minutes for _, minutes in schedule)} min')
    print('Tip: Take a short break between study sessions.')


def show_priorities(tasks):
    ranked = ranked_tasks(tasks)
    if not ranked:
        print('No pending tasks.')
        return
    for position, task in enumerate(ranked, start=1):
        print(f"{position}. {task['title']} ({task['subject']}) — "
              f"due {task['deadline']}")


def show_progress(tasks):
    total = len(tasks)
    completed = sum(task['completed'] for task in tasks)
    percent = completed / total * 100 if total else 0
    print(f'Completed: {completed}/{total} tasks ({percent:.1f}%)')


def main():
    tasks = load_tasks()
    actions = {
        '1': lambda: add_task(tasks),
        '2': lambda: view_tasks(tasks),
        '3': lambda: show_priorities(tasks),
        '4': lambda: show_schedule(tasks),
        '5': lambda: mark_complete(tasks),
        '6': lambda: delete_task(tasks),
        '7': lambda: show_progress(tasks),
    }
    while True:
        print('\n=== SmartStudy AI ===')
        print('1. Add task\n2. View tasks\n3. View priorities\n'
              '4. Generate study schedule\n5. Complete task\n'
              '6. Delete task\n7. View progress\n0. Exit')
        choice = input('Choose an option: ').strip()
        if choice == '0':
            print('Good luck with your studies!')
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print('Invalid option. Choose 0-7.')


if __name__ == '__main__':
    main()
