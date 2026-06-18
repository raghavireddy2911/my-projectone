tasks = []

# Load tasks from file
try:
    with open("tasks.txt", "r") as f:
        tasks = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    pass


def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")


while True:
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ").strip()
        if task == "":
            print("Task cannot be empty!")
        else:
            tasks.append(task)
            save_tasks()
            print("✅ Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    save_tasks()
                    print(f"❌ Removed: {removed}")
                else:
                    print("Invalid number!")
            except ValueError:
                print("Please enter a valid number!")

    elif choice == "4":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice! Try again.")
        