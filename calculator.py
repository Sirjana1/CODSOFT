
import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Shree's CALC")
      
        self.result_var = tk.StringVar()

        self.entry = tk.Entry(master, textvariable=self.result_var, justify="right", font=('Arial', 14))
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Define button layout and operations
        buttons = [
           ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), 
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), 
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), 
        ]
        # This is Sirjana practice code
        # Create and place buttons
        for (text, row, column) in buttons:
            button = tk.Button(master, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column, sticky="nsew")

        # Configure row and column weights so that they expand proportionally
        for i in range(5):
            master.grid_rowconfigure(i, weight=1)
            master.grid_columnconfigure(i, weight=1)

    def on_button_click(self, text):
        if text == '=':
            try:
                result = str(eval(self.result_var.get()))
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

