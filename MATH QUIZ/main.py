
import tkinter as tk
import random

score = 0
count = 0
attempt = 1

BG = "#E8E1F2"
PURPLE = "#7654A8"
LIGHT_PURPLE = "#D8C9EB"
WHITE = "#FFFFFF"
TEXT = "#383044"

def start():
    global score, count, digits

    score = 0
    count = 0

    level = choice.get()
    digits = 1 if level == "Easy" else 2 if level == "Medium" else 3

    score_label.config(text="Score: 0")
    question()

def question():
    global a, b, answer, attempt, count

    if count == 10:
        problem.config(text="Quiz Completed!")
        result.config(text=f"Final Score: {score}/100")
        submit_btn.config(state="disabled")
        return

    count += 1
    attempt = 1

    a = random.randint(10**(digits-1), 10**digits-1)
    b = random.randint(10**(digits-1), 10**digits-1)

    op = random.choice(["+", "-"])
    answer = a + b if op == "+" else a - b

    problem.config(text=f"{a} {op} {b} = ?")
    entry.delete(0, tk.END)

    progress.config(text=f"Question {count}/10")
    result.config(text="Enter your answer")
    submit_btn.config(state="normal")

def check():
    global score, attempt

    if not entry.get().lstrip("-").isdigit():
        result.config(text="Enter a valid number")
        return

    if int(entry.get()) == answer:
        score += 10 if attempt == 1 else 5
        score_label.config(text=f"Score: {score}")
        result.config(text="Correct!")
        root.after(700, question)

    elif attempt == 1:
        attempt = 2
        result.config(text="Wrong! Try again.")

    else:
        result.config(text=f"Correct answer: {answer}")
        root.after(1000, question)


root = tk.Tk()
root.title("Math Quiz")
root.geometry("520x650")
root.configure(bg=BG)
root.resizable(False, False)

tk.Label(
    root,
    text="MATH QUIZ",
    font=("Arial", 27, "bold"),
    bg=BG,
    fg=PURPLE
).pack(pady=(25, 5))

tk.Label(
    root,
    text="Test your addition and subtraction skills",
    font=("Arial", 11),
    bg=BG,
    fg=TEXT
).pack(pady=(0, 15))

# Difficulty box
difficulty_box = tk.Frame(root, bg=WHITE, padx=25, pady=15)
difficulty_box.pack(padx=40, fill="x", pady=10)

tk.Label(
    difficulty_box,
    text="CHOOSE DIFFICULTY",
    font=("Arial", 13, "bold"),
    bg=WHITE,
    fg=PURPLE
).pack(pady=5)

choice = tk.StringVar(value="Easy")

for level, color in [
    ("Easy", "#D8EEDC"),
    ("Medium", "#D8E8F7"),
    ("Hard", "#F4DCE8")
]:
    tk.Radiobutton(
        difficulty_box,
        text=level,
        variable=choice,
        value=level,
        font=("Arial", 11, "bold"),
        bg=color,
        fg=TEXT,
        selectcolor=color,
        activebackground=color,
        indicatoron=0,
        width=20,
        pady=7
    ).pack(pady=4)

tk.Button(
    difficulty_box,
    text="START QUIZ",
    command=start,
    bg=PURPLE,
    fg=WHITE,
    font=("Arial", 11, "bold"),
    relief="flat",
    width=20,
    pady=8,
    cursor="hand2"
).pack(pady=12)

# Score and progress
info_box = tk.Frame(root, bg=LIGHT_PURPLE, padx=15, pady=12)
info_box.pack(padx=40, fill="x", pady=10)

score_label = tk.Label(
    info_box,
    text="Score: 0",
    font=("Arial", 13, "bold"),
    bg=LIGHT_PURPLE,
    fg=PURPLE
)
score_label.pack(side="left")

progress = tk.Label(
    info_box,
    text="Question 0/10",
    font=("Arial", 11, "bold"),
    bg=LIGHT_PURPLE,
    fg=TEXT
)
progress.pack(side="right")

# Question box
question_box = tk.Frame(root, bg=WHITE, padx=20, pady=25)
question_box.pack(padx=40, fill="x", pady=10)

problem = tk.Label(
    question_box,
    text="Ready to play?",
    font=("Arial", 25, "bold"),
    bg=WHITE,
    fg=TEXT
)
problem.pack(pady=15)

entry = tk.Entry(
    question_box,
    font=("Arial", 18),
    justify="center",
    width=18,
    relief="solid",
    bd=1
)
entry.pack(ipady=7, pady=10)

submit_btn = tk.Button(
    question_box,
    text="SUBMIT ANSWER",
    command=check,
    bg=PURPLE,
    fg=WHITE,
    font=("Arial", 11, "bold"),
    relief="flat",
    width=20,
    pady=9,
    cursor="hand2"
)
submit_btn.pack(pady=10)

result = tk.Label(
    question_box,
    text="Choose a difficulty to begin",
    font=("Arial", 11),
    bg=WHITE,
    fg=PURPLE
)
result.pack(pady=5)

root.mainloop()
