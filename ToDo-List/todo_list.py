tasks = []


def add_task():

    title = input("Enter task description: ").strip()

    if title == "":
        print("Task description cannot be empty.")
        return

    task = {
        "title": title,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully.")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\n--- Your Tasks ---")
    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. {task['title']} [{status}]")


def mark_task_complete():
    if not tasks:
        print("No tasks available.")
        return

    view_tasks()

    try:
        task_number = int(input("Enter task number to mark as completed: "))

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return

        tasks[task_number - 1]["completed"] = True
        print("Task marked as completed.")
    except ValueError:
        print("Please enter a valid number.")

    view_tasks()

    try:
        task_number = int(input("Enter task number to mark as completed: "))

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return

        tasks[task_number - 1]["completed"] = True
        print("Task marked as completed.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    if not tasks:
        print("No tasks available.")
        return

    view_tasks()

    try:
        task_number = int(input("Enter task number to delete: "))

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return

        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task['title']}' deleted successfully.")
    except ValueError:
        print("Please enter a valid number.")


def main_menu():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting To-Do List...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()