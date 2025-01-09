from datetime import datetime

class Task:
    def __init__(self, task_id: int, description: str, due_date: datetime):
        self.task_id = task_id
        self.description = description
        self.due_date = due_date
        self.completed = False
    
    def mark_as_completed(self):
        self.completed = True
    
    def is_completed(self):
        return self.completed
    
    def __str__(self):
        status = "X" if self.completed else " "
        return f"[{status}] {self.task_id}: {self.description} (Due: {self.due_date})"