from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.statement = self.canvas.create_text(150,
                                                 125,
                                                 width=280,
                                                 text="Some Question text",
                                                 font=("Arial", 20, "italic")
                                                 )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_image, highlightthickness=0, bg=THEME_COLOR, command=self.is_true)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(image=false_image, highlightthickness=0, bg=THEME_COLOR, command=self.is_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.statement, text=q_text)
        else:
            self.canvas.itemconfig(self.statement, text="You've reached the end ot the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def is_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def is_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right is True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, func=self.get_next_question)
