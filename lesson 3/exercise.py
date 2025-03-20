todo_list = {}

def add_task(task): # Game Play
    task_id = len(todo_list) + 1 
    todo_list[task_id] = {"task": task, "done": False}
    print(f"Task '{task}' added successfully.")

def view_tasks():
    if not todo_list:
        print("No tasks available.")
    else:
        for task_id, details in todo_list.items():
            status = "✔ Done" if details["done"] else "❌ Not Done"
            print(f"{task_id}. {details['task']} - {status}")

def mark_done(task_id):
    if task_id in todo_list:
        todo_list[task_id]["done"] = True
        print(f"Task {task_id} marked as done.")
    else:
        print("Invalid Task ID.")

def delete_task(task_id):
    if task_id in todo_list:
        del todo_list[task_id]
        print(f"Task {task_id} deleted successfully.")
    else:
        print("Invalid Task ID.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter task: ") # Game Play
            add_task(task) # Game Play
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_id = int(input("Enter Task ID to mark as done: "))
            mark_done(task_id)
        elif choice == "4":
            task_id = int(input("Enter Task ID to delete: "))
            delete_task(task_id)
        elif choice == "5":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

