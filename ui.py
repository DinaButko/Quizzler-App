from tkinter import *


THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.title("Quizzler")

        self.label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question = self.canvas.create_text(150, 125, text="Question is", fill="black", font="Arial 20 italic")

        self.right_answer = PhotoImage(file="images/true.png")
        self.button_right = Button(image=self.right_answer, highlightbackground=THEME_COLOR)
        self.button_right.grid(column=0, row=2)
        self.wrong_answer = PhotoImage(file="images/false.png")
        self.button_wrong = Button(image=self.wrong_answer, highlightbackground=THEME_COLOR)
        self.button_wrong.grid(column=1, row=2)

        self.window.mainloop()
