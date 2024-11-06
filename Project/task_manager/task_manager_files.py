import json
from datetime import datetime

TASK_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASK_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "due_date": due_date,
        "status": "Incomplete"
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

def view_tasks():
    tasks = load_tasks()
    for task in tasks:
        print(f"ID: {task['id']}, Title: {task['title']}, Due Date: {task['due_date']}, Status: {task['status']}")

def update_task():
    task_id = int(input("Enter task ID to update: "))
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = input("Enter new title: ")
            task["description"] = input("Enter new description: ")
            task["due_date"] = input("Enter new due date (YYYY-MM-DD): ")
            task["status"] = input("Enter new status (Incomplete/Complete): ")
            save_tasks(tasks)
            print("Task updated!")
            return
    print("Task not found.")

def delete_task():
    task_id = int(input("Enter task ID to delete: "))
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print("Task deleted!")

def main():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
