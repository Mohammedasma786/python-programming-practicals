# SmartStudy AI 📚

A beginner-friendly, terminal-based **Python study planner** that helps students organize tasks, prioritize deadlines, and create personalized study schedules.

> **AI transparency:** Version 1 uses a transparent, rule-based prioritization algorithm, not a trained machine-learning model or a generative AI service.

## Features

- Add study tasks with subject, deadline, difficulty, importance, and estimated time
- View, complete, and delete tasks
- Rank pending tasks by urgency, importance, and difficulty
- Generate a daily study schedule based on available minutes
- Track task completion percentage
- Save tasks locally to `tasks.json`

## Tech stack

- Python 3.9+
- Python standard library (`datetime`, `json`, `pathlib`)
- JSON file storage

## Getting started

1. Install [Python](https://www.python.org/downloads/).
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

   ```bash
   python main.py
   ```

   On some macOS/Linux systems, use `python3 main.py`.

No `pip install` is necessary.

## Example workflow

1. Select **1** to add a task such as *Revise Python loops*.
2. Set a deadline, difficulty (1–5), importance (1–5), and estimated minutes.
3. Select **3** to view ranked priorities.
4. Select **4** and enter the minutes available today to create a schedule.
5. Select **5** to mark a finished task complete.
6. Select **7** to see your progress.

## How prioritization works

Each pending task receives a score:

`urgency + (importance × 5) + (difficulty × 3)`

Overdue tasks receive 50 urgency points; tasks due today receive 30; future tasks receive `max(0, 20 - 2 × days_until_due)`. Higher-scoring tasks are scheduled first, up to their estimated minutes. This is a heuristic, not an optimal or predictive AI model. Scheduling is for a single session and does not subtract already-studied time from the saved estimate.

## Project structure

```text
smartstudy-ai/
├── main.py          # Command-line menu and task management
├── planner.py       # Prioritization and schedule generation
├── storage.py       # JSON file persistence
├── requirements.txt # No external dependencies
├── .gitignore       # Ignore local data and Python cache
└── README.md        # Project documentation
```

## Roadmap

- [ ] Add editable tasks and remaining-time tracking
- [ ] Add a calendar interface
- [ ] Add a web interface using Streamlit
- [ ] Add optional AI-generated study suggestions
- [ ] Add automated tests

## Privacy

Task data stays on your computer in `tasks.json`, which is excluded from Git tracking by `.gitignore`.

## Author

Created as a first Python and software-development portfolio project.
