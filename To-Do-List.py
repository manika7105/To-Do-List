print("\n==========To-Do List==========")
todo_list = []

def add_task(task):
    todo_list.append({"task": task, "completed": False})
    print(f"Task '{task}' added!")

def show_tasks():
    if not todo_list:
        print("No tasks yet!")
        return
    print("Your Tasks:")
    task_number = 1
    for item in todo_list:
        if item["completed"]:
            status = "[X]"
        else:
            status = "[ ]"
        print(f"{task_number}. {status} {item['task']}")
        task_number += 1

def update_task(index, new_task):
    index = int(index) - 1
    if 0 <= index < len(todo_list):
        todo_list[index]["task"] = new_task
        print("Task updated!")
    else:
        print("Invalid task number.")

def delete_task(index):
    index = int(index) - 1
    if 0 <= index < len(todo_list):
        del todo_list[index]
        print("Task deleted!")
    else:
        print("Invalid task number.")

def mark_completed(index):
    index = int(index) - 1
    if 0 <= index < len(todo_list):
        todo_list[index]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

while True:
    print("\nOptions:")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Update task")
    print("4. Delete task")
    print("5. Mark task as completed")
    print("6. Quit")

    choice = input("Enter your choice(1-6): ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        index = input("Enter task number to update: ")
        new_task = input("Enter new task: ")
        update_task(index, new_task)
    elif choice == "4":
        index = input("Enter task number to delete: ")
        delete_task(index)
    elif choice == "5":
        index = input("Enter task number to mark completed: ")
        mark_completed(index)
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")


