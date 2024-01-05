import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoListGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Todo List")
        self.master.configure(bg="#add8e6")  # Light blue background
        self.todos = []

        # GUI components with basic styling
        self.label = tk.Label(master, text="Todo List", font=("Helvetica", 16, "bold"), pady=10, bg="DarkSalmon")
        self.label.pack()

        self.listbox = tk.Listbox(master, font=("Helvetica", 12), selectbackground="#a6a6a6", selectforeground="white", bg="LightSalmon")
        self.listbox.pack(expand=True, fill=tk.BOTH)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_todo, font=("Helvetica", 12), padx=10, pady=5, bg="#4CAF50", fg="white")
        self.add_button.pack()

        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_todo, font=("Helvetica", 12), padx=10, pady=5, bg="#4CAF50", fg="white")
        self.remove_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.destroy, font=("Helvetica", 12), padx=10, pady=5, bg="#4CAF50", fg="white")
        self.quit_button.pack()

    def show_todos(self):
        self.listbox.delete(0, tk.END)
        if not self.todos:
            self.listbox.insert(tk.END, "Todos not found")
        else:
            for task in self.todos:
                self.listbox.insert(tk.END, task)

    def add_todo(self):
        add_task = simpledialog.askstring("Add Task", "Enter the todo task:")
        if add_task:
            self.todos.append(add_task)
            self.show_todos()

    def remove_todo(self):
        selected_task_index = self.listbox.curselection()
        if not selected_task_index:
            messagebox.showinfo("Remove Task", "Please select a task to remove.")
            return

        remove_task = self.todos.pop(selected_task_index[0])
        messagebox.showinfo("Remove Task", f"Task '{remove_task}' removed from todo list.")
        self.show_todos()

def main():
    root = tk.Tk()
    root.geometry("400x400")  # Set the initial window size
    todo_list_gui = TodoListGUI(root)
    todo_list_gui.show_todos()  # Show initial tasks if any
    root.mainloop()

if __name__ == "__main__":
    main()
