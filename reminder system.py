from datetime import datetime, timedelta
import time
from collections import defaultdict

class ReminderSystem:
    def __init__(self):
        self.tasks = defaultdict(list)
        self.recurring_tasks = []
        
    def add_task(self, title, time_str, description="", recurring=False):
        try:
            # Parse time in HH:MM format
            task_time = datetime.strptime(time_str, "%H:%M").time()
            
            task = {
                'title': title,
                'time': task_time,
                'description': description,
                'completed': False
            }
            
            if recurring:
                self.recurring_tasks.append(task)
                print(f"Added recurring task: {title} at {time_str}")
            else:
                today = datetime.now().date()
                self.tasks[today].append(task)
                print(f"Added task: {title} for today at {time_str}")
                
        except ValueError:
            print("Invalid time format! Please use HH:MM (e.g., 14:30)")

    def list_today_tasks(self):
        today = datetime.now().date()
        all_tasks = self.tasks[today] + self.recurring_tasks
        
        if not all_tasks:
            print("\nNo tasks for today!")
            return
            
        print("\nToday's Tasks:")
        print("=" * 50)
        
        # Sort tasks by time
        sorted_tasks = sorted(all_tasks, key=lambda x: x['time'])
        
        current_time = datetime.now().time()
        
        for task in sorted_tasks:
            status = "✓" if task['completed'] else " "
            is_past = task['time'] < current_time
            time_str = task['time'].strftime("%H:%M")
            
            # Format the output
            if is_past and not task['completed']:
                status = "!"  # Overdue
                print(f"[{status}] {time_str} - {task['title']} (OVERDUE)")
            else:
                print(f"[{status}] {time_str} - {task['title']}")
                
            if task['description']:
                print(f"     {task['description']}")
                
        print("=" * 50)
        print("Legend: [ ] Pending, [✓] Completed, [!] Overdue")

    def mark_completed(self, task_title):
        today = datetime.now().date()
        found = False
        
        # Check today's tasks
        for task in self.tasks[today]:
            if task['title'].lower() == task_title.lower():
                task['completed'] = True
                found = True
                print(f"Marked '{task_title}' as completed!")
                
        # Check recurring tasks
        for task in self.recurring_tasks:
            if task['title'].lower() == task_title.lower():
                task['completed'] = True
                found = True
                print(f"Marked recurring task '{task_title}' as completed!")
                
        if not found:
            print(f"Task '{task_title}' not found!")

    def reset_recurring_tasks(self):
        """Reset recurring tasks at the start of each day"""
        for task in self.recurring_tasks:
            task['completed'] = False

    def show_menu(self):
        while True:
            print("\nDaily Reminder System")
            print("1. Add New Task")
            print("2. Add Recurring Task")
            print("3. List Today's Tasks")
            print("4. Mark Task as Completed")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == "1":
                title = input("Enter task title: ").strip()
                time_str = input("Enter time (HH:MM): ").strip()
                desc = input("Enter description (optional): ").strip()
                self.add_task(title, time_str, desc)
                
            elif choice == "2":
                title = input("Enter recurring task title: ").strip()
                time_str = input("Enter time (HH:MM): ").strip()
                desc = input("Enter description (optional): ").strip()
                self.add_task(title, time_str, desc, recurring=True)
                
            elif choice == "3":
                self.list_today_tasks()
                
            elif choice == "4":
                title = input("Enter task title to mark as completed: ").strip()
                self.mark_completed(title)
                
            elif choice == "5":
                print("Goodbye!")
                break
                
            else:
                print("Invalid choice! Please try again.")

def main():
    reminder = ReminderSystem()
    
    # Add some sample tasks
    reminder.add_task("Morning Meeting", "09:00", "Team standup")
    reminder.add_task("Lunch Break", "12:30")
    reminder.add_task("Exercise", "17:00", "30 minutes workout", recurring=True)
    
    # Start the menu
    reminder.show_menu()

if __name__ == "__main__":
    main()