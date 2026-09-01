import tkinter as tk
import random


# -----------------------------
# Game Logic
# -----------------------------

choices = ["Rock", "Paper", "Scissors"]

player_score = 0
computer_score = 0


def play_game(player_choice):
    global player_score, computer_score

    # Computer chooses randomly
    computer_choice = random.choice(choices)

    # Display choices
    player_choice_label.config(
        text=f"You chose: {player_choice}"
    )

    computer_choice_label.config(
        text=f"Computer chose: {computer_choice}"
    )

    # Determine winner
    if player_choice == computer_choice:
        result = "🤝 It's a Draw!"
        result_label.config(text=result)

    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or
        (player_choice == "Paper" and computer_choice == "Rock")
        or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        player_score += 1
        result = "🎉 You Win!"
        result_label.config(text=result)

    else:
        computer_score += 1
        result = "😢 Computer Wins!"
        result_label.config(text=result)

    # Update score
    score_label.config(
        text=f"You   {player_score}   -   {computer_score}   Computer"
    )


def reset_game():
    global player_score, computer_score

    player_score = 0
    computer_score = 0

    player_choice_label.config(text="You chose: -")
    computer_choice_label.config(text="Computer chose: -")
    result_label.config(text="Choose your move!")
    score_label.config(text="You   0   -   0   Computer")


# -----------------------------
# Main Window
# -----------------------------

window = tk.Tk()

window.title("Rock Paper Scissors")
window.geometry("650x600")
window.resizable(False, False)
window.configure(bg="#1e1e2f")


# -----------------------------
# Title
# -----------------------------

title_label = tk.Label(
    window,
    text="✊ Rock  📄 Paper  ✌️ Scissors",
    font=("Arial", 26, "bold"),
    bg="#1e1e2f",
    fg="white"
)

title_label.pack(pady=(35, 10))


subtitle_label = tk.Label(
    window,
    text="Choose your move!",
    font=("Arial", 15),
    bg="#1e1e2f",
    fg="#b8b8c7"
)

subtitle_label.pack(pady=(0, 25))


# -----------------------------
# Score
# -----------------------------

score_label = tk.Label(
    window,
    text="You   0   -   0   Computer",
    font=("Arial", 20, "bold"),
    bg="#292940",
    fg="#ffffff",
    padx=30,
    pady=15
)

score_label.pack(pady=10)


# -----------------------------
# Choices
# -----------------------------

choices_frame = tk.Frame(
    window,
    bg="#1e1e2f"
)

choices_frame.pack(pady=30)


rock_button = tk.Button(
    choices_frame,
    text="✊\nRock",
    font=("Arial", 16, "bold"),
    width=10,
    height=3,
    bg="#3b3b5c",
    fg="white",
    activebackground="#50507a",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=lambda: play_game("Rock")
)

rock_button.grid(row=0, column=0, padx=10)


paper_button = tk.Button(
    choices_frame,
    text="📄\nPaper",
    font=("Arial", 16, "bold"),
    width=10,
    height=3,
    bg="#3b3b5c",
    fg="white",
    activebackground="#50507a",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=lambda: play_game("Paper")
)

paper_button.grid(row=0, column=1, padx=10)


scissors_button = tk.Button(
    choices_frame,
    text="✌️\nScissors",
    font=("Arial", 16, "bold"),
    width=10,
    height=3,
    bg="#3b3b5c",
    fg="white",
    activebackground="#50507a",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=lambda: play_game("Scissors")
)

scissors_button.grid(row=0, column=2, padx=10)


# -----------------------------
# Results
# -----------------------------

player_choice_label = tk.Label(
    window,
    text="You chose: -",
    font=("Arial", 14),
    bg="#1e1e2f",
    fg="#dddddd"
)

player_choice_label.pack(pady=(10, 5))


computer_choice_label = tk.Label(
    window,
    text="Computer chose: -",
    font=("Arial", 14),
    bg="#1e1e2f",
    fg="#dddddd"
)

computer_choice_label.pack(pady=5)


result_label = tk.Label(
    window,
    text="Choose your move!",
    font=("Arial", 22, "bold"),
    bg="#1e1e2f",
    fg="#ffd166"
)

result_label.pack(pady=20)


# -----------------------------
# Reset Button
# -----------------------------

reset_button = tk.Button(
    window,
    text="🔄  Reset Game",
    font=("Arial", 13, "bold"),
    bg="#e05a5a",
    fg="white",
    activebackground="#f06b6b",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    padx=20,
    pady=10,
    command=reset_game
)

reset_button.pack(pady=10)


# -----------------------------
# Footer
# -----------------------------

footer_label = tk.Label(
    window,
    text="Python Programming Fundamentals • File 48",
    font=("Arial", 10),
    bg="#1e1e2f",
    fg="#77778c"
)

footer_label.pack(side="bottom", pady=15)


# -----------------------------
# Start Application
# -----------------------------

window.mainloop()