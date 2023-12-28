THEME_COLOR = "#375362"

THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question = self.canvas.create_text(150, 125, text="text", font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        true = PhotoImage(file="images/true.png")
        false = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true, highlightthickness=0, command=self.true_button)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=false, highlightthickness=0, command=self.false_button)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            quest = self.quiz.next_question()
            self.canvas.configure(bg="white")
            self.canvas.itemconfig(self.question, text=quest)
        else:
            self.canvas.configure(bg="white")
            self.canvas.itemconfig(self.question, text="END OF QUIZ")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")



    def true_button(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)
        # self.score_label.config(text=f"Score: {self.quiz.score}")

    def false_button(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)
        # self.score_label.config(text=f"Score: {self.quiz.score}")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)
