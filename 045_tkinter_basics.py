###########################################################
# Tkinter Basics in Python
###########################################################


"""
Tkinter is Python's built-in library
for creating Graphical User Interfaces (GUI).

GUI means:

Graphical User Interface

Examples:

- Windows
- Buttons
- Labels
- Text boxes

Tkinter is included with Python,
so usually we don't need to install it.
"""


# ===========================================================
# PART 1: Import Tkinter
# ===========================================================


import tkinter as tk


# ===========================================================
# PART 2: Create a Window
# ===========================================================


window = tk.Tk()


# Set window title

window.title("My First Application")


# Set window size

window.geometry("500x400")


# ===========================================================
# PART 3: Label
# ===========================================================


"""
Label is used to display text
inside the window.
"""


label = tk.Label(
    window,
    text="Welcome to Python Course"
)


label.pack()



# ===========================================================
# PART 4: Button
# ===========================================================


"""
Button allows the user
to perform an action.
"""


button = tk.Button(
    window,
    text="Click Me"
)


button.pack()



# ===========================================================
# PART 5: Entry
# ===========================================================


"""
Entry is used to receive
text input from the user.
"""


entry = tk.Entry(window)


entry.pack()



# ===========================================================
# PART 6: Function with Button
# ===========================================================


def say_hello():

    print("Hello!")


hello_button = tk.Button(
    window,
    text="Say Hello",
    command=say_hello
)


hello_button.pack()



# ===========================================================
# PART 7: Get Input from Entry
# ===========================================================


def get_name():

    name = entry.get()

    print("Hello", name)


name_button = tk.Button(
    window,
    text="Submit Name",
    command=get_name
)


name_button.pack()



# ===========================================================
# PART 8: Display Result in Label
# ===========================================================


result_label = tk.Label(
    window,
    text=""
)


result_label.pack()



def show_name():

    name = entry.get()

    result_label.config(
        text=f"Hello {name}"
    )


show_button = tk.Button(
    window,
    text="Show Name",
    command=show_name
)


show_button.pack()



# ===========================================================
# PART 9: Simple Addition Application
# ===========================================================


number1_entry = tk.Entry(window)

number1_entry.pack()


number2_entry = tk.Entry(window)

number2_entry.pack()


addition_result = tk.Label(
    window,
    text=""
)

addition_result.pack()



def add_numbers():

    number1 = float(
        number1_entry.get()
    )

    number2 = float(
        number2_entry.get()
    )

    result = number1 + number2

    addition_result.config(
        text=f"Result: {result}"
    )


add_button = tk.Button(
    window,
    text="Add Numbers",
    command=add_numbers
)


add_button.pack()



# ===========================================================
# PART 10: Important Widgets
# ===========================================================


"""
Tk()

Creates the main window.


Label

Displays text.


Button

Creates a clickable button.


Entry

Allows the user to enter text.


pack()

Places widgets inside the window.


config()

Changes widget properties.


mainloop()

Keeps the window running.
"""


# ===========================================================
# PART 11: Run the Application
# ===========================================================


window.mainloop()



# ===========================================================
# PART 12: Practice Exercises
# ===========================================================


"""
Exercise 1:

Create a window with:

- Title
- Size
- Label


-----------------------------------------------------------


Exercise 2:

Create a button.

When the user clicks the button,
print:

Hello Python


-----------------------------------------------------------


Exercise 3:

Create:

- Entry
- Button
- Label

Ask the user to enter their name.

When clicking the button,
display:

Hello [Name]


-----------------------------------------------------------


Exercise 4:

Create a simple calculator.

Ask the user to enter:

- Number 1
- Number 2

Create buttons for:

+
-
*
/

Display the result.


-----------------------------------------------------------


Exercise 5:

Create a simple application that asks for:

Name
Age

When the user clicks Submit,
display the entered information.
"""


###########################################################
# END OF TKINTER BASICS
###########################################################
