from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#7FBCD2"



class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.title("Quizzler")

        self.label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question = self.canvas.create_text(150, 125, text="Question is", fill="black", font="Arial 20 italic", width=250)

        self.right_answer = PhotoImage(file="images/true.png")
        self.button_right = Button(image=self.right_answer, highlightbackground=THEME_COLOR, command=self.true_pressed)
        self.button_right.grid(column=0, row=2)
        self.wrong_answer = PhotoImage(file="images/false.png")
        self.button_wrong = Button(image=self.wrong_answer, highlightbackground=THEME_COLOR, command=self.false_pressed)
        self.button_wrong.grid(column=1, row=2)
        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the Quizz")
            self.button_right.config(state="disabled")
            self.button_wrong.config(state="disabled")


    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_wrong = self.quiz.check_answer("False")
        self.give_feedback(is_wrong)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)