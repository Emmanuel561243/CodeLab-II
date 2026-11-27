
import tkinter as tk
import random
import os

BG = "#101B35"
RED = "#E62429"
BLUE = "#1768AC"
LIGHT_BLUE = "#DCEBFA"
WHITE = "#FFFFFF"
BLACK = "#151515"

current_punchline = ""

def tell_joke():
    global current_punchline

    try:
        file_path = os.path.join(os.path.dirname(__file__), "randomJokes.txt")

        with open(file_path, "r", encoding="utf-8") as file:
            jokes = file.readlines()

        jokes = [joke.strip() for joke in jokes if "?" in joke]

        if not jokes:
            setup_label.config(text="No jokes found!")
            return

        joke = random.choice(jokes)
        setup, current_punchline = joke.split("?", 1)

        setup_label.config(text=setup.lstrip("- ").strip())
        punchline_label.config(text="")
        result.config(text="Click SHOW PUNCHLINE to reveal the answer.")

    except FileNotFoundError:
        setup_label.config(text="randomJokes.txt not found!")
        punchline_label.config(text="")

def show_punchline():
    if current_punchline:
        punchline_label.config(text=current_punchline.strip())
        result.config(text="Hope you enjoyed the joke!")

root = tk.Tk()
root.title("Alexa Tell Me a Joke")
root.geometry("520x700")
root.configure(bg=BG)
root.resizable(False, False)

header = tk.Frame(root, bg=RED, pady=20)
header.pack(fill="x")

tk.Label(
    header,
    text="ALEXA",
    font=("Arial", 23, "bold"),
    bg=RED,
    fg=WHITE
).pack()



tk.Label(
    root,
    text="READY FOR A LAUGH?",
    font=("Arial", 11, "bold"),
    bg=BG,
    fg=LIGHT_BLUE
).pack(pady=15)

joke_box = tk.Frame(
    root,
    bg=WHITE,
    padx=25,
    pady=25,
    highlightbackground=RED,
    highlightthickness=3
)
joke_box.pack(padx=35, fill="x", pady=10)

tk.Label(
    joke_box,
    text="YOUR JOKE",
    font=("Arial", 14, "bold"),
    bg=WHITE,
    fg=RED
).pack(pady=10)

setup_label = tk.Label(
    joke_box,
    text="Click the button to get a joke!",
    font=("Arial", 17, "bold"),
    bg=WHITE,
    fg=BLACK,
    wraplength=390,
    justify="center"
)
setup_label.pack(pady=25)

punchline_box = tk.Frame(
    root,
    bg=LIGHT_BLUE,
    padx=20,
    pady=20,
    highlightbackground=BLUE,
    highlightthickness=3
)
punchline_box.pack(padx=35, fill="x", pady=10)

tk.Label(
    punchline_box,
    text="PUNCHLINE",
    font=("Arial", 13, "bold"),
    bg=LIGHT_BLUE,
    fg=BLUE
).pack(pady=5)

punchline_label = tk.Label(
    punchline_box,
    text="Waiting for the punchline...",
    font=("Arial", 14),
    bg=LIGHT_BLUE,
    fg=BLACK,
    wraplength=390,
    justify="center"
)
punchline_label.pack(pady=15)

tk.Button(
    root,
    text="ALEXA, TELL ME A JOKE",
    command=tell_joke,
    bg=RED,
    fg=WHITE,
    activebackground="#B71920",
    activeforeground=WHITE,
    font=("Arial", 11, "bold"),
    relief="flat",
    width=25,
    pady=10,
    cursor="hand2"
).pack(pady=7)

tk.Button(
    root,
    text="SHOW PUNCHLINE",
    command=show_punchline,
    bg=BLUE,
    fg=WHITE,
    activebackground="#104B80",
    activeforeground=WHITE,
    font=("Arial", 11, "bold"),
    relief="flat",
    width=25,
    pady=10,
    cursor="hand2"
).pack(pady=7)

tk.Button(
    root,
    text="NEXT JOKE",
    command=tell_joke,
    bg=WHITE,
    fg=RED,
    activebackground=LIGHT_BLUE,
    activeforeground=RED,
    font=("Arial", 11, "bold"),
    relief="flat",
    width=25,
    pady=10,
    cursor="hand2"
).pack(pady=7)

result = tk.Label(
    root,
    text="",
    font=("Arial", 9, "bold"),
    bg=BG,
    fg=LIGHT_BLUE
)
result.pack(pady=12)

root.mainloop()
