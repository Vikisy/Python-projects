import tkinter as tk
import random
from _functools import partial

# Quiz data
questions = [
    {
        "q": "What is the primary objective of Artificial Intelligence (AI)?",
        "options": ["A) To replace all human jobs",
                    "B) To simulate human intelligence to perform tasks and solve problems",
                    "C) To design faster computer hardware"],
        "answer": "B"
    },
    {
        "q": "Which of these is not a branch of Artificial Intelligence?",
        "options": ["A) Natural Language Processing",
                    "B) Robotics",
                    "C) Quantum Physics"],
        "answer": "C"
    },
    {
        "q": "Which of the following is an example of supervised learning?",
        "options": ["A) Randomly generating data for analysis",
                    "B) Training a model to classify emails as spam or not spam",
                    "C) Allowing an agent to learn by trial and error"],
        "answer": "B"
    },
    {
        "q": "What is the main purpose of data preprocessing in Machine Learning?",
        "options": ["A) To clean and prepare data for better model performance",
                    "B) To slow down model training for accuracy",
                    "C) To increase data redundancy"],
        "answer": "A"
    },
    {
        "q": "Which programming language is most widely used for Artificial Intelligence and Machine Learning?",
        "options": ["A) Java",
                    "B) C++",
                    "C) Python"],
        "answer": "C"
    }
]

random.shuffle(questions)

# QUIZ LOGIC
class AIQuizApp:
    def __init__(self):
        self.root = root
        self.root.title("AI Quiz App")
        self.root.geometry("700x450")
        self.root.config(bg="#101820")

        self.current_question = 0
        self.score = 0

        # Question label
        self.question_label = tk.Label(
            root, text="", wraplength=650,
            font=("TkDefaultFont", 16, "bold"),
            bg="#101820", fg="white", justify="left"
        )
        self.question_label.pack(pady=30)

        # Option button
        self.option_buttons = []
        for q_opt in range(3):
            btn = tk.Button(
                root, text="", wraplength=650,
                font=("TkDefaultFont", 14),
                width=55, relief="raised",  justify="left",
                command=partial(self.check_answer, q_opt))
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        # Feedback label
        self.feedback_label = tk.Label(
            root, text="",
            font=("TkDefaultFont", 16, "italic"),
            bg="#101820", fg="lightgreen"
        )
        self.feedback_label.pack(pady=10)

        self.feedback_label2 = tk.Label(
            root, text="", wraplength=650,
            font=("TkDefaultFont", 16, "italic"),
            bg="#101820", fg="lightgreen"
        )
        self.feedback_label2.pack()

        # Next button
        self.next_button = tk.Button(
            root, text="Next Question",
            font=("TkDefaultFont", 12, "bold"),
            bg="lightblue", state="disabled",
            command=self.next_question
        )
        self.next_button.pack(pady=15)

        # Start quiz
        self.show_question()

    def show_question(self):
        self.feedback_label.config(text="")
        self.feedback_label2.config(text="")
        self.next_button.config(state="disabled")

        # Check if quiz is finished
        if self.current_question >= len(questions):
            self.show_result()
            return

        q_data = questions[self.current_question]

        self.question_label.config(
            text=f"Q{self.current_question + 1}: {q_data['q']}"
        )

        for i, opt in enumerate(q_data["options"]):
            self.option_buttons[i].config(
                text=opt, state="normal",
                bg="#E0FFFF", fg="black"
            )

    def check_answer(self, index):
        q_data = questions[self.current_question]
        selected_option = q_data["options"][index]
        correct_letter = q_data["answer"]
        correct_text = next(
            opt for opt in q_data["options"] if opt.startswith(correct_letter)
        )

        # Disable buttons to prevent re-answering
        for btn in self.option_buttons:
            btn.config(state="disabled")

        # Evaluate the answer (Feedback)
        if selected_option.startswith(correct_letter):
            self.score +=1
            self.feedback_label.config(text="✅ Correct!", fg="lightgreen")
            self.option_buttons[index].config(bg="lightgreen")

        else:
            self.feedback_label.config(
                text=f"❌ Incorrect!", fg="red"
            )
            self.feedback_label2.config(
                text=f"Correct answer: {correct_text}", fg="green"
            )
            self.option_buttons[index].config(bg="#FAA0A0")

        if self.current_question < len(questions) - 1:
            self.next_button.config(state="normal")
        else:
            self.next_button.config(text="Show Result", state="normal")

    def next_question(self):
        self.current_question +=1
        self.show_question()

    def show_result(self):
        for btn in self.option_buttons:
            btn.pack_forget()
        self.next_button.pack_forget()
        self.feedback_label.config(text="")
        self.question_label.config(
            text=f"Quiz Completed!\n\nYour final score: {self.score}/{len(questions)}",
            font=("TkDefaultFont", 20, "bold"), fg="lightblue",
            justify="center"
        )
        self.question_label.pack(pady=150)

    def restart_quiz(self):
        random.shuffle(questions)
        self.current_question = 0
        self.score = 0

        for btn in self.option_buttons:
            btn.pack(pady=5)
        self.next_button.pack(pady=15)

if __name__ == "__main__":
    root = tk.Tk()
    app = AIQuizApp()
    root.mainloop()