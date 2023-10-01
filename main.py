from tkinter import *
from tkinter import messagebox
import random

BACKGROUND_COLOR = "#8EACCD"
duration = 60

window = Tk()
window.title("Typing_speed")
window.geometry("800x800")
window.config(padx=50, pady=50)

# Read the list of strings from a file and choose a random string
with open('word_list.txt', 'r') as file:
    my_strings_list = file.readlines()
my_strings_list = [string.strip() for string in my_strings_list]
my_string = random.choice(my_strings_list)


# Function to calculate typing speed
def speed():
    score = 0
    words = typing_entry.get()
    words_list = words.split()
    string_list = text.split()

    num_comparisons = min(len(words_list), len(string_list))
    for i in range(num_comparisons):
        if words_list[i] == string_list[i]:
            score += 1

    if score > 0:
        cpm = len(words) + 1
    else:
        cpm = 0
    results.itemconfig(results_txt, text=f" WPM : {score}  \n CPM: {cpm} \n Mistakes: \n")


# Function to start the game
def start():
    global duration
    typing_entry.config(state='normal')
    typing_entry.focus()
    if duration > 0:
        canvas.itemconfig(timer_txt, text=f"Time remaining :{duration}")
        duration -= 1
        window.after(1000, start)
    if duration == 0:
        results.grid(row=6, column=0, pady=10)
        speed()
        messagebox.showinfo(message="Time's up!")
        typing_entry.delete(0, 'end')
        duration = 10
        canvas.itemconfig(timer_txt, text=f"Time remaining : 00")


# Function to exit the game
# def exit_the_game():
#     x = messagebox.askokcancel(title="Bye!", message="You are about to quit the game")
#     if x:
#         exit()


with open("word_list.txt", "r", encoding='UTF-8') as words:
    word_list = [word.strip() for word in words.read().split(",")]
    random.shuffle(word_list)

window.title("Typing Speed Tester")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

welcome_text = Label(window, text="Test your Typing Speed", fg="#FF6969", font=("Impact", 25), bg=BACKGROUND_COLOR)
welcome_text.grid(row=0, column=0)

# Create a Canvas for the timer
canvas = Canvas(window, width=700, height=60, bg="grey", highlightthickness=5)
timer_txt = canvas.create_text(300, 30, text="Time remaining :60", fill="white", font=("courier", 30, "bold"))
canvas.grid(row=1, column=0, pady=10)

text = " ".join(word_list[:100])
text_canvas = Canvas(window, width=700, height=220, bg="#FFCC70", highlightthickness=1)
my_text = text_canvas.create_text(350, 100, text=text, fill="black", font=("courier", 12, "bold"), width=650,
                                  anchor="center")
text_canvas.grid(row=2, column=0, padx=30, pady=30)

rules = Label(
    window,
    text="1. You have to type the words displayed above\n2.You will get one minute to type\n"
         "3.The counting will start as soon as you start to type",
    fg="indigo",
    font=("Helvetica", 15, "italic"),
    bg=BACKGROUND_COLOR
)
rules.grid(row=3, column=0)

typing_entry = Entry(window, font=("Helvetica", 15), width=50, state='disabled', justify='center')
typing_entry.grid(row=4, column=0, pady=10)

# Create a LabelFrame for buttons
border = LabelFrame(window, bd=3, bg="white")
border.grid(pady=5)

# # Create a Quit button
# speed_btn = Button(border, text="QUIT", command=exit_the_game, width=15,
#                    height=2, fg="white", background="red", font=("Times New Roman", 13))
# speed_btn.grid(side="left", padx=20)

# Create a Start button
start_btn = Button(border, text="Start game", command=start, height=2, width=15,
                   fg="white", background="green",
                   font=("Times New Roman", 13))
start_btn.grid(row=5, column=0)

# Create a Canvas for displaying results
results = Canvas(window, width=400, height=300, bg="grey")
results_txt = results.create_text(150, 100, text=" WPM :  \n CPM: \n \n", fill="white",
                                  font=("courier", 15, "bold"), width=250
                                  )

window.mainloop()
