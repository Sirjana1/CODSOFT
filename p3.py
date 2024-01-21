import tkinter as tk
from tkinter import messagebox

class QuizGUI:
    def __init__(self, master, questions):
        self.master = master
        self.questions = questions
        self.score = 0
        self.current_question = 0

        # GUI elements
        self.question_label = tk.Label(master, text="")
        self.radio_var = tk.IntVar()
        self.radio_buttons = []
        self.submit_button = tk.Button(master, text="Submit", command=self.check_answer)

        self.setup_gui()

    def setup_gui(self):
        self.master.title("Quiz GUI")
        self.question_label.pack()

        for i in range(4):
            radio_button = tk.Radiobutton(self.master, text="", variable=self.radio_var, value=i+1)
            self.radio_buttons.append(radio_button)
            radio_button.pack()

        self.submit_button.pack()

        self.display_question()

    def display_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data['question'])

            for i in range(4):
                self.radio_buttons[i].config(text=question_data['options'][i])

        else:
            self.display_result()

    def check_answer(self):
        user_answer = self.radio_var.get()

        if user_answer == self.questions[self.current_question]['correct_option']:
            self.score += 1

        self.current_question += 1
        self.radio_var.set(0)  # Reset radio button selection

        self.display_question()

    def display_result(self):
        messagebox.showinfo("Quiz Result", f"You scored {self.score} out of {len(self.questions)}.")

# Sample questions for the quiz
questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['Paris', 'Berlin', 'Madrid', 'Rome'],
        'correct_option': 1
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'options': ['Mars', 'Venus', 'Jupiter', 'Saturn'],
        'correct_option': 1
    },
    {
        'question': 'What is the largest mammal?',
        'options': ['Elephant', 'Blue Whale', 'Giraffe', 'Hippopotamus'],
        'correct_option': 2
    }
]

# Create Tkinter window and QuizGUI object
root = tk.Tk()
quiz_gui = QuizGUI(root, questions)

# Start the Tkinter event loop
root.mainloop()
input_number = input("Enter a number:")

if input_number == '1':
    # Display the GUI screen
    print("Displaying GUI screen")
elif input_number.lower() == 'exit':
    # Stay on the coding terminal
    print("Staying on the coding terminal")
else:
    # Handle other cases
    print("Invalid input. Please enter '1' to display GUI or 'exit' to stay on the coding terminal.")
