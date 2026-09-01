import tkinter as tk


# -------------------------
# Game Variables
# -------------------------

current_player = "X"
game_over = False

buttons = []


# -------------------------
# Check Winner
# -------------------------

def check_winner():

    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:

        if (
            buttons[a]["text"] != ""
            and buttons[a]["text"]
            == buttons[b]["text"]
            == buttons[c]["text"]
        ):
            return buttons[a]["text"]

    return None


# -------------------------
# Check Draw
# -------------------------

def check_draw():

    for button in buttons:

        if button["text"] == "":
            return False

    return True


# -------------------------
# Button Click
# -------------------------

def button_click(index):

    global current_player
    global game_over

    # Stop the game if it is over
    if game_over:
        return

    # Don't allow changing an occupied button
    if buttons[index]["text"] != "":
        return

    # Add X or O
    buttons[index]["text"] = current_player

    # Check winner
    winner = check_winner()

    if winner:

        result_label.config(
            text=f"🎉 Player {winner} Wins!"
        )

        game_over = True

        return

    # Check draw
    if check_draw():

        result_label.config(
            text="🤝 It's a Draw!"
        )

        game_over = True

        return

    # Change player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    result_label.config(
        text=f"Player {current_player}'s Turn"
    )


# -------------------------
# Reset Game
# -------------------------

def reset_game():

    global current_player
    global game_over

    current_player = "X"
    game_over = False

    # Clear all buttons
    for button in buttons:
        button.config(text="")

    # Reset message
    result_label.config(
        text="Player X's Turn"
    )


# -------------------------
# Create Window
# -------------------------

window = tk.Tk()

window.title("XO Game")
window.geometry("500x650")

window.config(bg="#22223b")

window.resizable(False, False)


# -------------------------
# Title
# -------------------------

title_label = tk.Label(
    window,
    text="⭕ XO Game ❌",
    font=("Arial", 30, "bold"),
    bg="#22223b",
    fg="white"
)

title_label.pack(pady=(30, 10))


# -------------------------
# Result Label
# -------------------------

result_label = tk.Label(
    window,
    text="Player X's Turn",
    font=("Arial", 18, "bold"),
    bg="#22223b",
    fg="#ffd166"
)

result_label.pack(pady=20)


# -------------------------
# Game Board
# -------------------------

game_frame = tk.Frame(
    window,
    bg="#22223b"
)

game_frame.pack()


# -------------------------
# Create 9 Buttons
# -------------------------

for i in range(9):

    button = tk.Button(
        game_frame,
        text="",
        font=("Arial", 30, "bold"),
        width=5,
        height=2,
        bg="#4a4e69",
        fg="white",
        activebackground="#6c7086",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        command=lambda i=i: button_click(i)
    )

    button.grid(
        row=i // 3,
        column=i % 3,
        padx=5,
        pady=5
    )

    buttons.append(button)


# -------------------------
# Play Again Button
# -------------------------

reset_button = tk.Button(
    window,
    text="🔄  Play Again",
    font=("Arial", 15, "bold"),
    bg="#ef476f",
    fg="white",
    activebackground="#d9365e",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    width=18,
    pady=10,
    command=reset_game
)

reset_button.pack(pady=25)


# -------------------------
# Footer
# -------------------------

footer_label = tk.Label(
    window,
    text="Python Programming Fundamentals • File 49",
    font=("Arial", 10),
    bg="#22223b",
    fg="#888899"
)

footer_label.pack(side="bottom", pady=15)


# -------------------------
# Start Program
# -------------------------

window.mainloop()