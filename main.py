from tkinter import *
import time

BACKGROUND_COLOR = "#8EACCD"

with open("word_list.txt", "r", encoding='UTF-8') as words:
    word_list = [word.strip() for word in words.read().split(",")]

window = Tk()
window.title("Typing Speed Tester")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

welcome_text = Label(text="Test your Typing Speed", fg="#FF6969", font=("Impact", 25), bg=BACKGROUND_COLOR)
welcome_text.grid(row=0, column=0)

canvas = Canvas(height=50, width=600, bg="white", highlightthickness=0)
canvas.grid(row=1, column=0, padx=50, pady=50)

rules = Label(
    text="1. You have to type the words displayed above\n2.You will get one minute to type\n"
         "3.The counting will start as soon as you start to type",
    fg="indigo",
    font=("Ariel", 15),
    bg=BACKGROUND_COLOR
)
rules.grid(row=2, column=0)

typing_area = Text(highlightthickness=0, height=2, width=40)
typing_area.grid(row=3, column=0, pady=50)

window.mainloop()
