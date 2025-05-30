from tkinter import *
import random
from tkinter import messagebox
from word import easy_words, medium_words, hard_words

Mainscreen = Tk()
Mainscreen.geometry('950x650')
Mainscreen.title('Typing Test')
Mainscreen.config(bg="light blue")

score = 0
missed = 0
time = 0
count1 = 0
movingwords = ''
current_difficulty = "Easy"

# Load the high score from a file
try:
    with open('highscore.txt', 'r') as file:
        high_score = int(file.read())
except FileNotFoundError:
    high_score = 0

# Function to update the moving text
def movingtext():
    global count1, movingwords
    floatingtext = 'Typing Test'
    if count1 >= len(floatingtext):
        count1 = 0
        movingwords = ''
    movingwords += floatingtext[count1]
    count1 += 1
    fontlabel.configure(text=movingwords)
    fontlabel.after(150, movingtext)

# Function to handle the timer
def giventime():
    global time, score, missed, high_score
    if time > 11:
        pass
    else:
        timercount.configure(fg='red')
    if time > 0:
        time -= 1
        timercount.configure(text=time)
        timercount.after(1000, giventime)
    else:
        gameinstruction.configure(text='Hit = {} | Miss = {} | Total Score = {} | High Score = {}'
                                   .format(score, missed, score - missed, high_score))
        if score > high_score:
            high_score = score
            with open('highscore.txt', 'w') as file:
                file.write(str(high_score))
        rr = messagebox.askretrycancel('Notification', 'Do you want to play again?')
        if rr:
            score = 0
            missed = 0
            time = int(time_var.get())  # Reset time based on user selection
            timercount.configure(text=time)
            labelforward.configure(text=get_random_word(), fg=get_random_color())
            scorelabelcount.configure(text=score)
            wordentry.delete(0, END)
            giventime()

# Function to handle the game logic
def game(event):
    global score, missed
    if time == 0:
        giventime()
    gameinstruction.configure(text='')
    startlabel.configure(text='')
    if wordentry.get() == labelforward['text']:
        score += 1
        scorelabelcount.configure(text=score)
    else:
        missed += 1
    labelforward.configure(text=get_random_word(), fg=get_random_color())
    wordentry.delete(0, END)

# Function to get a random word based on difficulty level
def get_random_word():
    if current_difficulty == "Easy":
        return random.choice(easy_words)
    elif current_difficulty == "Medium":
        return random.choice(medium_words)
    elif current_difficulty == "Hard":
        return random.choice(hard_words)

# Function to get a random color
def get_random_color():
    colors = ['red', 'blue', 'green', 'purple', 'orange', 'brown','light blue','light pink','pink']
    return random.choice(colors)

# Function to handle the difficulty level change
def change_difficulty(*args):
    global current_difficulty
    current_difficulty = difficulty_var.get()
    labelforward.configure(text=get_random_word(), fg=get_random_color())

# Function to start the game with user-specified settings
def start_game():
    global time, score, missed
    time = int(time_var.get())
    score = 0
    missed = 0
    timercount.configure(text=time)
    labelforward.configure(text=get_random_word(), fg=get_random_color())
    scorelabelcount.configure(text=score)
    wordentry.delete(0, END)
    giventime()

def get_username():
    username = username_entry.get()
    startlabel.configure(text=f'Hello, {username}! Start Typing')
    labelforward.configure(text=get_random_word(), fg=get_random_color())
    start_game()

# Create and place the components
fontlabel = Label(Mainscreen, text='', font=('arial', 25, 'italic bold'), fg='purple', width=45)
fontlabel.place(x=15, y=10)
movingtext()

username_label = Label(Mainscreen, text='Enter your username:', font=('arial', 20, 'bold'), bg='orange', fg='black')
username_label.place(x=75, y=100)

username_entry = Entry(Mainscreen, font=('arial', 20, 'italic bold'), bd=10, justify='center')
username_entry.place(x=75, y=150)
username_entry.focus_set()

difficulty_label = Label(Mainscreen, text='Select Difficulty:', font=('arial', 18, 'bold'), bg='light blue', fg='black')
difficulty_label.place(x=530, y=100)

difficulty_options = ["Easy", "Medium", "Hard"]
difficulty_var = StringVar()
difficulty_var.set(difficulty_options[0])
difficulty_menu = OptionMenu(Mainscreen, difficulty_var, *difficulty_options, command=change_difficulty)
difficulty_menu.config(font=('arial', 18), bg='sky blue')
difficulty_menu.place(x=730, y=100)

time_label = Label(Mainscreen, text='Select Time(sec):', font=('arial', 18, 'bold'), bg='light blue', fg='black')
time_label.place(x=530, y=150)

time_options = [15, 30, 45, 60]
time_var = StringVar()
time_var.set(str(time_options[0]))
time_menu = OptionMenu(Mainscreen, time_var, *map(str, time_options))
time_menu.config(font=('arial', 18), bg='sky blue')
time_menu.place(x=730, y=150)

start_button = Button(Mainscreen, text='Start', font=('arial', 18, 'bold'), command=get_username)
start_button.place(x=200, y=220)

startlabel = Label(Mainscreen, text='', font=('arial', 20, 'italic bold'), bg='black', fg='white')
startlabel.place(x=250, y=300)

labelforward = Label(Mainscreen, text=get_random_word(), font=('arial', 45, 'italic bold'), fg=get_random_color())
labelforward.place(x=250, y=380)

scorelabel = Label(Mainscreen, text='Your Score:', font=('arial', 25, 'italic bold'), fg='red')
scorelabel.place(x=20, y=285)

scorelabelcount = Label(Mainscreen, text=score, font=('arial', 25, 'italic bold'), fg='blue')
scorelabelcount.place(x=160, y=335)

labelfortimer = Label(Mainscreen, text='Time Left:', font=('arial', 25, 'italic bold'), fg='red')
labelfortimer.place(x=630, y=280)

timercount = Label(Mainscreen, text=time, font=('arial', 25, 'italic bold'), fg='blue')
timercount.place(x=630, y=330)

gameinstruction = Label(Mainscreen, text='Hit enter button after typing the word', font=('caveat', 25), fg='grey')
gameinstruction.place(x=140, y=540)

wordentry = Entry(Mainscreen, font=('arial', 25, 'italic bold'), bd=10, justify='center')
wordentry.place(x=230, y=470)
wordentry.focus_set()

Mainscreen.bind('<Return>', game)
Mainscreen.mainloop()
