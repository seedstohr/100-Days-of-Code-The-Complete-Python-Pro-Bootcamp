from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Monospace"
WHITE = "#f9f9f9"
CROSS_IMAGE = "./images/false.png"
CHECK_MARK_IMAGE ="./images/true.png"

class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.question = self.canvas.create_text(150, 125, text=f"questions",
                                                       font=(FONT_NAME, 10, "italic"), width= 280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score = Label(text=f"Score: 0", bg=THEME_COLOR, fg=WHITE, font=(FONT_NAME, 15))
        self.score.grid(row=0, column=1)

        self.right_image = PhotoImage(file=CHECK_MARK_IMAGE)
        self.wrong_image = PhotoImage(file=CROSS_IMAGE)

        self.button_right = Button(image=self.right_image, highlightthickness=0, bg=THEME_COLOR, command=self.button_true)
        self.button_right.grid(row=2, column=0)

        self.button_wrong = Button(image=self.wrong_image, highlightthickness=0, bg=THEME_COLOR, command=self.button_false)
        self.button_wrong.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg=WHITE)
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You have reached the end.")
            self.button_right.config(state="disabled")
            self.button_wrong.config(state="disabled")

    def button_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def button_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)





