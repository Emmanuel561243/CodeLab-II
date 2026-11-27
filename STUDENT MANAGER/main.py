
import tkinter as tk
from tkinter import ttk

students = [
    {"code": "8439", "name": "Jake Hobbs", "mark1": 10, "mark2": 11, "mark3": 10, "exam": 43},
    {"code": "1234", "name": "John Smith", "mark1": 15, "mark2": 18, "mark3": 17, "exam": 75},
    {"code": "5678", "name": "Mary Jane", "mark1": 12, "mark2": 14, "mark3": 16, "exam": 60}
]

BG = "#EDF3FA"
BLUE = "#1769AA"
DARK = "#123456"
LIGHT = "#E1EDFA"
WHITE = "#FFFFFF"
TEXT = "#26374A"
GREEN = "#21865B"
RED = "#D94B4B"


def get_results(s):
    coursework = s["mark1"] + s["mark2"] + s["mark3"]
    total = coursework + s["exam"]
    percentage = total / 160 * 100

    if percentage >= 70:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    return coursework, total, percentage, grade


def show_student(s):
    coursework, total, percentage, grade = get_results(s)

    output.insert(tk.END, f"  {s['name']}\n", "heading")
    output.insert(tk.END, f"  Student Number: {s['code']}\n")
    output.insert(tk.END, f"  Coursework: {coursework}/60\n")
    output.insert(tk.END, f"  Exam: {s['exam']}/100\n")
    output.insert(tk.END, f"  Total: {total}/160\n")
    output.insert(tk.END, f"  Percentage: {percentage:.2f}%\n")
    output.insert(tk.END, f"  Grade: {grade}\n", "grade")
    output.insert(tk.END, "  " + "─" * 43 + "\n\n", "line")


def clear_output():
    output.delete("1.0", tk.END)


def display_title(title):
    clear_output()
    output.insert(tk.END, f"\n  {title}\n", "title")
    output.insert(tk.END, "  " + "═" * 43 + "\n\n", "line")


def view_all():
    display_title("ALL STUDENT RESULTS")

    total_percentage = 0

    for s in students:
        show_student(s)
        total_percentage += get_results(s)[2]

    average = total_percentage / len(students)

    output.insert(tk.END, f"\n  Number of students: {len(students)}\n", "heading")
    output.insert(tk.END, f"  Class average: {average:.2f}%\n", "grade")


def view_one():
    name = search.get().strip().lower()

    if not name:
        display_title("SEARCH STUDENT")
        output.insert(tk.END, "  Please enter a student name or number.")
        return

    for s in students:
        if name == s["name"].lower() or name == s["code"]:
            display_title("STUDENT DETAILS")
            show_student(s)
            return

    display_title("SEARCH RESULTS")
    output.insert(tk.END, "  Student not found!\n\n", "error")
    output.insert(tk.END, "  Please check the name or student number.")


def highest():
    s = max(students, key=lambda x: get_results(x)[1])

    display_title("HIGHEST SCORING STUDENT")
    show_student(s)


def lowest():
    s = min(students, key=lambda x: get_results(x)[1])

    display_title("LOWEST SCORING STUDENT")
    show_student(s)


def reset():
    search.delete(0, tk.END)
    clear_output()
    output.insert(tk.END, "\n  Welcome to Student Manager!\n\n", "title")
    output.insert(tk.END, "  Select an option from the left menu to begin.\n")
    output.insert(tk.END, "\n  You can view all students, search for an\n")
    output.insert(tk.END, "  individual student, or compare scores.\n")


root = tk.Tk()
root.title("Student Manager")
root.geometry("900x720")
root.minsize(750, 620)
root.configure(bg=BG)

style = ttk.Style()
style.theme_use("clam")
style.configure(
    "Vertical.TScrollbar",
    background=LIGHT,
    troughcolor=BG,
    bordercolor=BG,
    arrowcolor=BLUE
)

# Header
header = tk.Frame(root, bg=DARK, height=100)
header.pack(fill="x")
header.pack_propagate(False)

tk.Label(
    header,
    text="STUDENT MANAGER",
    font=("Arial", 25, "bold"),
    bg=DARK,
    fg=WHITE
).pack(anchor="w", padx=30, pady=(18, 2))

tk.Label(
    header,
    text="Student Performance Dashboard",
    font=("Arial", 11),
    bg=DARK,
    fg="#C7DDF5"
).pack(anchor="w", padx=32)

# Dashboard statistics
stats = tk.Frame(root, bg=BG)
stats.pack(fill="x", padx=20, pady=15)

average = sum(get_results(s)[2] for s in students) / len(students)
top_student = max(students, key=lambda x: get_results(x)[1])
bottom_student = min(students, key=lambda x: get_results(x)[1])

def create_stat(parent, label, value, color):
    card = tk.Frame(parent, bg=WHITE, highlightbackground="#D7E2EF",
                    highlightthickness=1)
    card.pack(side="left", fill="both", expand=True, padx=5)

    tk.Label(
        card, text=label, font=("Arial", 9, "bold"),
        bg=WHITE, fg="#64788E"
    ).pack(pady=(13, 3))

    tk.Label(
        card, text=value, font=("Arial", 19, "bold"),
        bg=WHITE, fg=color
    ).pack(pady=(0, 13))


create_stat(stats, "TOTAL STUDENTS", str(len(students)), BLUE)
create_stat(stats, "CLASS AVERAGE", f"{average:.2f}%", GREEN)
create_stat(stats, "HIGHEST SCORE", f"{get_results(top_student)[2]:.2f}%", GREEN)
create_stat(stats, "LOWEST SCORE", f"{get_results(bottom_student)[2]:.2f}%", RED)

# Main content
main = tk.Frame(root, bg=BG)
main.pack(fill="both", expand=True, padx=20, pady=5)

# Left menu
menu = tk.Frame(main, bg=WHITE, width=245,
                highlightbackground="#D7E2EF", highlightthickness=1)
menu.pack(side="left", fill="y", padx=(0, 12))
menu.pack_propagate(False)

tk.Label(
    menu, text="MENU", font=("Arial", 15, "bold"),
    bg=WHITE, fg=DARK
).pack(anchor="w", padx=18, pady=(22, 15))


def make_button(text, command, color=BLUE):
    btn = tk.Button(
        menu,
        text=text,
        command=command,
        font=("Arial", 10, "bold"),
        bg=color,
        fg=WHITE,
        activebackground=DARK,
        activeforeground=WHITE,
        relief="flat",
        cursor="hand2",
        height=2
    )
    btn.pack(fill="x", padx=15, pady=6)


make_button("View All Students", view_all)
make_button("Highest Score", highest, GREEN)
make_button("Lowest Score", lowest, RED)

tk.Label(
    menu,
    text="SEARCH STUDENT",
    font=("Arial", 10, "bold"),
    bg=WHITE,
    fg=DARK
).pack(anchor="w", padx=18, pady=(25, 8))

search = tk.Entry(
    menu,
    font=("Arial", 11),
    bg="#F3F7FC",
    fg=TEXT,
    relief="flat",
    highlightthickness=1,
    highlightbackground="#B9CCE0"
)
search.pack(fill="x", padx=15, ipady=9)

make_button("Search Student", view_one)
search.bind("<Return>", lambda event: view_one())

make_button("Clear / Reset", reset, "#687C91")

tk.Label(
    menu,
    text="Search by name or student number.",
    font=("Arial", 8),
    bg=WHITE,
    fg="#75869A",
    wraplength=200
).pack(anchor="w", padx=18, pady=12)

# Results panel
panel = tk.Frame(main, bg=WHITE,
                 highlightbackground="#D7E2EF", highlightthickness=1)
panel.pack(side="left", fill="both", expand=True)

tk.Label(
    panel,
    text="STUDENT RESULTS",
    font=("Arial", 15, "bold"),
    bg=WHITE,
    fg=DARK
).pack(anchor="w", padx=18, pady=(20, 3))

tk.Label(
    panel,
    text="View student marks and performance",
    font=("Arial", 9),
    bg=WHITE,
    fg="#75869A"
).pack(anchor="w", padx=18, pady=(0, 12))

result_frame = tk.Frame(panel, bg=WHITE)
result_frame.pack(fill="both", expand=True, padx=15, pady=(0, 15))

scrollbar = ttk.Scrollbar(result_frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

output = tk.Text(
    result_frame,
    font=("Consolas", 10),
    bg="#F5F8FC",
    fg=TEXT,
    relief="flat",
    wrap="word",
    padx=12,
    pady=12,
    yscrollcommand=scrollbar.set,
    state="normal"
)
output.pack(side="left", fill="both", expand=True)
scrollbar.config(command=output.yview)

output.tag_config("title", font=("Arial", 13, "bold"), foreground=BLUE)
output.tag_config("heading", font=("Arial", 11, "bold"), foreground=DARK)
output.tag_config("grade", font=("Arial", 10, "bold"), foreground=GREEN)
output.tag_config("error", font=("Arial", 11, "bold"), foreground=RED)
output.tag_config("line", foreground="#A9BBD0")

reset()

root.mainloop()
