# Task Tracker

<a href="https://roadmap.sh/projects/task-tracker">Task tracker</a> is a project used to track and manage your tasks. In this task, you will build a simple command line interface (CLI) to track what you need to do, what you have done, and what you are currently working on. This project will help you practice your programming skills, including working with the filesystem, handling user inputs, and building a simple CLI application.

## ✨ Features

- Add a Task: Create tasks with descriptions. Each task gets a unique ID and a default todo status.
- Update a Task: Modify the description or status of a task.
- Mark as Todo: Quickly change a task’s status to todo.
- Mark as In-Progress: Quickly change a task’s status to in-progress.
- Mark as Done: Quickly change a task’s status to done.
- Delete a Task: Remove tasks by their ID.
- List Tasks: Display all tasks or filter them by:
  - status: todo, in-progress, done, or all

## ⚡ Installation

You can install Task Tracker directly from GitHub:

```sh
pip install git+https://github.com/6GinT0/Task-Tracker.git
```

## 🚀 Usage

```bash
$ task-cli add "description"

$ task-cli update id "description"

$ task-cli delete id

$ task-cli list [todo|in-progress|done]

$ task-cli mark-todo id

$ task-cli mark-in-progress id

$ task-cli mark-done id
```

## 📜 License

This project is licensed under the **MIT License**.
You are free to use, modify, and distribute it.
