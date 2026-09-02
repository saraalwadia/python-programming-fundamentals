import tkinter as tk
import random


# -------------------------
# Game Settings
# -------------------------

WIDTH = 600
HEIGHT = 400
SIZE = 20
SPEED = 100


# -------------------------
# Game Variables
# -------------------------

snake = [
    [100, 100],
    [80, 100],
    [60, 100]
]

food = [300, 200]
direction = "Right"
score = 0
game_over = False


# -------------------------
# Create Window
# -------------------------

window = tk.Tk()

window.title("Snake Game")
window.geometry("700x700")
window.config(bg="#22223b")
window.resizable(False, False)


# -------------------------
# Title
# -------------------------

title_label = tk.Label(
    window,
    text="🐍 Snake Game",
    font=("Arial", 28, "bold"),
    bg="#22223b",
    fg="white"
)

title_label.pack(pady=15)


# -------------------------
# Score
# -------------------------

score_label = tk.Label(
    window,
    text="Score: 0",
    font=("Arial", 16, "bold"),
    bg="#22223b",
    fg="#ffd166"
)

score_label.pack(pady=5)


# -------------------------
# Game Canvas
# -------------------------

canvas = tk.Canvas(
    window,
    width=WIDTH,
    height=HEIGHT,
    bg="#11111f",
    highlightthickness=0
)

canvas.pack(pady=10)


# -------------------------
# Change Direction
# -------------------------

def change_direction(new_direction):

    global direction

    if new_direction == "Up" and direction != "Down":
        direction = "Up"

    elif new_direction == "Down" and direction != "Up":
        direction = "Down"

    elif new_direction == "Left" and direction != "Right":
        direction = "Left"

    elif new_direction == "Right" and direction != "Left":
        direction = "Right"


# -------------------------
# Create Food
# -------------------------

def create_food():

    global food

    while True:

        x = random.randrange(0, WIDTH, SIZE)
        y = random.randrange(0, HEIGHT, SIZE)

        new_food = [x, y]

        # Make sure food is not inside snake
        if new_food not in snake:

            food = new_food
            break


# -------------------------
# Draw Game
# -------------------------

def draw_game():

    canvas.delete("all")

    # -------------------------
    # Draw Snake
    # -------------------------

    for i, part in enumerate(snake):

        x = part[0]
        y = part[1]

        if i == 0:

            # Snake Head
            canvas.create_rectangle(
                x,
                y,
                x + SIZE,
                y + SIZE,
                fill="#06d6a0",
                outline="#11111f"
            )

        else:

            # Snake Body
            canvas.create_rectangle(
                x,
                y,
                x + SIZE,
                y + SIZE,
                fill="#118ab2",
                outline="#11111f"
            )

    # -------------------------
    # Draw Food
    # -------------------------

    x = food[0]
    y = food[1]

    canvas.create_oval(
        x + 2,
        y + 2,
        x + SIZE - 2,
        y + SIZE - 2,
        fill="#ef476f",
        outline=""
    )


# -------------------------
# Game Over
# -------------------------

def end_game():

    global game_over

    game_over = True

    # -------------------------
    # Game Over Box
    # -------------------------

    canvas.create_rectangle(
        150,
        100,
        450,
        300,
        fill="#22223b",
        outline="#ef476f",
        width=3
    )

    # -------------------------
    # Game Over Text
    # -------------------------

    canvas.create_text(
        WIDTH // 2,
        145,
        text="GAME OVER",
        font=("Arial", 30, "bold"),
        fill="white"
    )

    # -------------------------
    # Final Score
    # -------------------------

    canvas.create_text(
        WIDTH // 2,
        195,
        text=f"Score: {score}",
        font=("Arial", 20, "bold"),
        fill="#ffd166"
    )

    # -------------------------
    # Restart Message
    # -------------------------

    canvas.create_text(
        WIDTH // 2,
        235,
        text="Click Restart to play again",
        font=("Arial", 13),
        fill="white"
    )

    # Show Restart Button
    restart_button.pack(pady=10)


# -------------------------
# Restart Game
# -------------------------

def restart_game():

    global snake
    global food
    global direction
    global score
    global game_over

    # -------------------------
    # Reset Snake
    # -------------------------

    snake = [
        [100, 100],
        [80, 100],
        [60, 100]
    ]

    # -------------------------
    # Reset Direction
    # -------------------------

    direction = "Right"

    # -------------------------
    # Reset Score
    # -------------------------

    score = 0

    score_label.config(
        text="Score: 0"
    )

    # -------------------------
    # Reset Game Over
    # -------------------------

    game_over = False

    # Hide Restart Button
    restart_button.pack_forget()

    # Create New Food
    create_food()

    # Draw Game
    draw_game()

    # Start Game
    move_snake()


# -------------------------
# Restart Button
# -------------------------

restart_button = tk.Button(
    window,
    text="🔄 Restart Game",
    font=("Arial", 14, "bold"),
    bg="#ef476f",
    fg="white",
    activebackground="#d9365e",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    width=18,
    pady=8,
    command=restart_game
)

# Hide button at the beginning
restart_button.pack_forget()


# -------------------------
# Move Snake
# -------------------------

def move_snake():

    global game_over
    global score

    if game_over:
        return

    # -------------------------
    # Get Head Position
    # -------------------------

    head_x = snake[0][0]
    head_y = snake[0][1]

    # -------------------------
    # Move Snake
    # -------------------------

    if direction == "Up":
        head_y -= SIZE

    elif direction == "Down":
        head_y += SIZE

    elif direction == "Left":
        head_x -= SIZE

    elif direction == "Right":
        head_x += SIZE

    new_head = [head_x, head_y]

    # -------------------------
    # Check Wall Collision
    # -------------------------

    if (
        head_x < 0
        or head_x >= WIDTH
        or head_y < 0
        or head_y >= HEIGHT
    ):

        end_game()
        return

    # -------------------------
    # Check Body Collision
    # -------------------------

    if new_head in snake:

        end_game()
        return

    # -------------------------
    # Add New Head
    # -------------------------

    snake.insert(0, new_head)

    # -------------------------
    # Check Food
    # -------------------------

    if new_head == food:

        # Increase Score
        score += 1

        score_label.config(
            text=f"Score: {score}"
        )

        # Create New Food
        create_food()

    else:

        # Remove Tail
        snake.pop()

    # -------------------------
    # Draw Game
    # -------------------------

    draw_game()

    # -------------------------
    # Move Again
    # -------------------------

    window.after(
        SPEED,
        move_snake
    )


# -------------------------
# Keyboard Controls
# -------------------------

window.bind(
    "<Up>",
    lambda event: change_direction("Up")
)

window.bind(
    "<Down>",
    lambda event: change_direction("Down")
)

window.bind(
    "<Left>",
    lambda event: change_direction("Left")
)

window.bind(
    "<Right>",
    lambda event: change_direction("Right")
)


# -------------------------
# Start Game
# -------------------------

create_food()

draw_game()

move_snake()

window.mainloop()