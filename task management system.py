from datetime import datetime, timedelta

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.priority_levels = {'high': 3, 'medium': 2, 'low': 1}

    def add_task(self, title, priority, days_to_complete):
        due_date = datetime.now() + timedelta(days=days_to_complete)
        task = {
            'title': title,
            'priority': priority,
            'due_date': due_date,
            'completed': False,
            'created_at': datetime.now()
        }
        self.tasks.append(task)
        print(f"Added task: {title}")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        print("\nCurrent Tasks:")
        print("-" * 50)
        
        # Sort tasks by priority (high to low) and due date
        sorted_tasks = sorted(
            self.tasks,
            key=lambda x: (-self.priority_levels[x['priority']], x['due_date'])
        )

        for task in sorted_tasks:
            status = "✓" if task['completed'] else " "
            due_date_str = task['due_date'].strftime('%Y-%m-%d')
            print(f"[{status}] {task['title']}")
            print(f"    Priority: {task['priority'].title()}")
            print(f"    Due: {due_date_str}")
            print(f"    {'COMPLETED' if task['completed'] else 'PENDING'}")
            print("-" * 50)

    def mark_completed(self, title):
        for task in self.tasks:
            if task['title'].lower() == title.lower():
                task['completed'] = True
                print(f"Marked '{title}' as completed!")
                return
        print(f"Task '{title}' not found.")

    def get_overdue_tasks(self):
        now = datetime.now()
        overdue = [task for task in self.tasks 
                  if not task['completed'] and task['due_date'] < now]
        
        if overdue:
            print("\nOverdue Tasks:")
            for task in overdue:
                days_overdue = (now - task['due_date']).days
                print(f"- {task['title']} ({days_overdue} days overdue)")
        else:
            print("\nNo overdue tasks!")

def main():
    manager = TaskManager()
    
    # Add sample tasks
    manager.add_task("Complete project proposal", "high", 2)
    manager.add_task("Review code changes", "medium", 3)
    manager.add_task("Update documentation", "low", 5)
    manager.add_task("Team meeting preparation", "high", 1)
    
    # Mark a task as completed
    manager.mark_completed("Review code changes")
    
    # List all tasks
    manager.list_tasks()
    
    # Check overdue tasks
    manager.get_overdue_tasks()

if __name__ == "__main__":
    main()