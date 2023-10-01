from tkinter import *
import time

BACKGROUND_COLOR = "#8EACCD"

with open("word_list.txt", "r", encoding='UTF-8') as words:
    word_list = [word.strip() for word in words.read().split(",")]

window = Tk()
window.title("Typing Speed Tester")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

welcome_text = Label(text="Test your Typing Speed", fg="white", font=("dff", 25, "italic"), bg=BACKGROUND_COLOR)
welcome_text.grid(row=0, column=0)

window.mainloop()
