from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # lable
        self.score_lable = Label(text="Score:0", bg=THEME_COLOR, fg="white")
        self.score_lable.grid(row=0, column=1)
        # canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="Some Questions",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50)
        # btn 1
        self.btn_img_true = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=self.btn_img_true, highlightthickness=0, command=self.true_pressed)
        self.true_btn.grid(row=2, column=0)
        # btn 2
        self.btn_img_false = PhotoImage(file="./images/false.png")
        self.false_btn = Button(image=self.btn_img_false, highlightthickness=0, command=self.false_pressed)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_lable.config(text=f"Score: {self.quiz.score} ")
            next_question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=next_question)
        else:
            self.canvas.itemconfig(self.question_text, text="You havce reached the end of the quiz")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def false_pressed(self):
        isRight = self.quiz.check_answer("False")
        self.give_feedback(isRight)


    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)


