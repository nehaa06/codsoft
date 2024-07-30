tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' has been added to the list.")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' has been removed from the list.")
    else:
        print(f"Task '{task}' not found in the list.")

def update_task(old_task, new_task):
    if old_task in tasks:
        index = tasks.index(old_task)
        tasks[index] = new_task
        print(f"Task '{old_task}' has been updated to '{new_task}'.")
    else:
        print(f"Task '{old_task}' not found in the list.")
def show_tasks():
    if tasks:
        print("Tasks in the To-Do list:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("The To-Do List is empty.")

while True:
    print("\nThe To-Do List App Menu:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Show tasks")
    print("4. Update a task")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '3':
        show_tasks()
    elif choice == '4':
        old_task = input("Enter the task to update: ")
        new_task = input("Enter the new task: ")
        update_task(old_task, new_task)
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please choose a valid option.")