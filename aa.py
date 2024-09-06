import os

def load_tasks(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]
    return []

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    filename = 'tasks.txt'
    tasks = load_tasks(filename)
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            save_tasks(filename, tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
