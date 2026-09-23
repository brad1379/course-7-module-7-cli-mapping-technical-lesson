# lib/models.py

class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def complete(self):
        self.completed = True
        print(f"✅ Task '{self.title}' marked as complete.")


class User:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"📌 Task '{task.title}' added to {self.name}'s task list.")

    def get_task_by_title(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
            else:
                return None
