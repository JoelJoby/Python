tasks = []

def add_task():
    title = input("Enter the task title: ")
    description = input("Enter the task description: ")
    tasks.append({"title": title, "description": description})
    print("Task Added Successfully")

def view_task():
    if tasks:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1): 
            print(f"{idx}. Title: {task['title']}, Description: {task['description']}")
    else:
        print("No tasks available")

def update_task():
    view_task()
    if tasks:
        task_index = int(input("Enter the index of the task to be updated: ")) - 1
        if 0 <= task_index < len(tasks):
            new_title = input("Enter the new title (press Enter to skip): ")
            new_description = input("Enter the new description (press Enter to skip): ")
            
            if new_title:
                tasks[task_index]['title'] = new_title
            if new_description:
                tasks[task_index]['description'] = new_description
            print("Task updated successfully.")
        else:
            print("Invalid task index.")
    else:
        print("No tasks available")

def delete_task():
    view_task()
    if tasks:
        task_index = int(input("Enter the index of the task to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            print(f"Task '{deleted_task['title']}' deleted successfully.")
        else:
            print("Invalid task index.")
    else:
        print("No tasks available")

def main():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
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

