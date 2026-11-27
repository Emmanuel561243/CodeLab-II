import tkinter as tk
import random

score = 0
count = 0
attempt = 1
answer = 0
digits = 1

BG = "#FFE5E5"
RED = "#C62828"
DARK_RED = "#8E0000"
WHITE = "#FFFFFF"
TEXT = "#222222"

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

    if count >= 10:
        problem.config(text="QUIZ COMPLETED!")
        result.config(text=f"Final Score: {score}/100")
        submit_btn.config(state="disabled")
        entry.config(state="disabled")
        return

    count += 1
    attempt = 1

    a = random.randint(10**(digits-1), 10**digits-1)
    b = random.randint(10**(digits-1), 10**digits-1)

    op = random.choice(["+", "-"])
    answer = a + b if op == "+" else a - b

    problem.config(text=f"{a} {op} {b} = ?")
    entry.config(state="normal")
    entry.delete(0, tk.END)
    entry.focus_set()

    progress.config(text=f"Question {count}/10")
    result.config(text="Type your answer below")
    submit_btn.config(state="normal")

def check(event=None):
    global score, attempt

    if submit_btn["state"] == "disabled":
        return "break"

    user_answer = entry.get().strip()

    if user_answer == "" or not user_answer.lstrip("-").isdigit():
        result.config(text="Please enter a number!")
        entry.focus_set()
        return "break"

    if int(user_answer) == answer:
        score += 10 if attempt == 1 else 5
        score_label.config(text=f"Score: {score}")
        result.config(text="Correct! Well done!")
        submit_btn.config(state="disabled")
        entry.config(state="disabled")
        root.after(1000, question)

    elif attempt == 1:
        attempt = 2
        result.config(text="Wrong! Try again.")
        entry.delete(0, tk.END)
        entry.focus_set()

    else:
        result.config(text=f"Correct answer: {answer}")
        submit_btn.config(state="disabled")
        entry.config(state="disabled")
        root.after(1500, question)

    return "break"


root = tk.Tk()
root.title("Math Quiz")
root.geometry("700x850")
root.configure(bg=BG)
root.resizable(False, False)

tk.Label(
    root,
    text="MATH QUIZ",
    font=("Arial", 36, "bold"),
    bg=BG,
    fg=RED
).pack(pady=20)


difficulty_box = tk.Frame(root, bg=WHITE, padx=20, pady=10)
difficulty_box.pack(padx=50, fill="x", pady=10)

tk.Label(
    difficulty_box,
    text="CHOOSE DIFFICULTY",
    font=("Arial", 16, "bold"),
    bg=WHITE,
    fg=RED
).pack(pady=5)

choice = tk.StringVar(value="Easy")

for level in ["Easy", "Medium", "Hard"]:
    tk.Radiobutton(
        difficulty_box,
        text=level,
        variable=choice,
        value=level,
        font=("Arial", 13),
        bg=WHITE,
        fg=TEXT,
        selectcolor="#FFCCCC"
    ).pack()

tk.Button(
    difficulty_box,
    text="START QUIZ",
    command=start,
    bg=RED,
    fg=WHITE,
    font=("Arial", 14, "bold"),
    relief="flat",
    width=20,
    pady=8
).pack(pady=8)

info_box = tk.Frame(root, bg="#FFCCCC", padx=20, pady=12)
info_box.pack(padx=50, fill="x", pady=10)

score_label = tk.Label(
    info_box,
    text="Score: 0",
    font=("Arial", 15, "bold"),
    bg="#FFCCCC",
    fg=DARK_RED
)
score_label.pack(side="left")

progress = tk.Label(
    info_box,
    text="Question 0/10",
    font=("Arial", 14, "bold"),
    bg="#FFCCCC",
    fg=TEXT
)
progress.pack(side="right")

question_box = tk.Frame(root, bg=WHITE, padx=20, pady=20)
question_box.pack(padx=50, fill="both", expand=True, pady=10)

problem = tk.Label(
    question_box,
    text="Ready to play?",
    font=("Arial", 32, "bold"),
    bg=WHITE,
    fg=TEXT
)
problem.pack(pady=20)

tk.Label(
    question_box,
    text="YOUR ANSWER:",
    font=("Arial", 16, "bold"),
    bg=WHITE,
    fg=RED
).pack(pady=5)

entry = tk.Entry(
    question_box,
    font=("Arial", 25),
    justify="center",
    width=15,
    bg=WHITE,
    fg="black",
    insertbackground="black",
    relief="solid",
    bd=3
)
entry.pack(pady=15, ipady=12)

submit_btn = tk.Button(
    question_box,
    text="SUBMIT ANSWER",
    command=check,
    bg=RED,
    fg=WHITE,
    activebackground=DARK_RED,
    activeforeground=WHITE,
    font=("Arial", 16, "bold"),
    relief="raised",
    width=20,
    pady=12,
    cursor="hand2"
)
submit_btn.pack(pady=15)

result = tk.Label(
    question_box,
    text="Choose a difficulty to begin",
    font=("Arial", 15, "bold"),
    bg=WHITE,
    fg=RED
)
result.pack(pady=10)

root.mainloop()