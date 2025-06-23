import os

TASK_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from file."""
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as f:
        return [task.strip() for task in f.readlines()]

def save_tasks(tasks):
    """Save tasks to file."""
    with open(TASK_FILE, 'w') as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks found.\n")
    else:
        print("\n📋 Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

def add_task():
    task = input("Enter the new task: ").strip()
    if task:
        with open(TASK_FILE, 'a') as f:
            f.write(task + "\n")
        print("✅ Task added successfully.")
    else:
        print("⚠️ Task cannot be empty.")

def delete_task():
    tasks = load_tasks()
    show_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                save_tasks(tasks)
                print(f"🗑️ Task '{removed}' deleted.")
            else:
                print("❌ Invalid task number.")
        except ValueError:
            print("❌ Please enter a valid number.")

def main():
    while True:
        print("\n=== 📝 TO-DO LIST MENU ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            tasks = load_tasks()
            show_tasks(tasks)
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("👋 Exiting... Have a productive day!")
            break
        else:
            print("❌ Invalid choice. Please enter 1–4.")

if __name__ == "__main__":
    main()