# Todo List Application

todos = []

def show_todos():
    if not todos:
        print("No tasks in the todo list.")
    else:
        print("Todo List:")
        for index, task in enumerate(todos, start=1):
            print(f"{index}. {task}")

def add_todo():
    task = input("Enter a new task: ")
    todos.append(task)
    print(f"Task '{task}' added to the todo list.")

def remove_todo():
    show_todos()
    if not todos:
        return

    try:
        index = int(input("Enter the number of the task to remove: "))
        if 1 <= index <= len(todos):
            removed_task = todos.pop(index - 1)
            print(f"Task '{removed_task}' removed from the todo list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    while True:
        print("\nTodo List Menu:")
        print("1. Show Todo List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_todos()
        elif choice == '2':
            add_todo()
        elif choice == '3':
            remove_todo()
        elif choice == '4':
            print("Exiting the Todo List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
