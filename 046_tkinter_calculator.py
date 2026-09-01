###########################################################
# Tkinter Calculator Project
###########################################################


"""
Simple Calculator using Tkinter.

Features:

- Number buttons
- Addition +
- Subtraction -
- Multiplication *
- Division /
- Decimal point .
- Equal button =
- Delete last character
- Clear all
- Replace operation if two operations are entered
"""


# ===========================================================
# PART 1: Import Tkinter
# ===========================================================


import tkinter as tk


# ===========================================================
# PART 2: Create Main Window
# ===========================================================


window = tk.Tk()

window.title("Calculator")

window.geometry("400x550")

window.resizable(False, False)


# ===========================================================
# PART 3: Calculator Display
# ===========================================================


display = tk.Entry(
    window,
    font=("Arial", 25),
    justify="right"
)

display.pack(
    fill="x",
    padx=20,
    pady=20,
    ipady=15
)


# ===========================================================
# PART 4: Operations List
# ===========================================================


operators = ["+", "-", "*", "/"]


# ===========================================================
# PART 5: Add Number
# ===========================================================


def add_number(number):

    current_value = display.get()

    display.insert(
        tk.END,
        number
    )


# ===========================================================
# PART 6: Add Decimal Point
# ===========================================================


def add_decimal():

    current_value = display.get()

    # If the display is empty,
    # start with 0.

    if current_value == "":

        display.insert(
            tk.END,
            "0."
        )

        return


    # Get the last number after an operator

    last_number = current_value


    for operator in operators:

        if operator in last_number:

            last_number = last_number.split(operator)[-1]


    # Prevent multiple decimal points
    # in the same number

    if "." not in last_number:

        display.insert(
            tk.END,
            ".")


# ===========================================================
# PART 7: Add Operator
# ===========================================================


def add_operator(operator):

    current_value = display.get()


    # Do nothing if display is empty

    if current_value == "":

        return


    last_character = current_value[-1]


    # If the last character is already
    # an operator, replace it with
    # the new operator.

    if last_character in operators:

        new_value = current_value[:-1] + operator

        display.delete(
            0,
            tk.END
        )

        display.insert(
            0,
            new_value
        )


    else:

        display.insert(
            tk.END,
            operator
        )


# ===========================================================
# PART 8: Delete Last Character
# ===========================================================


def delete_last():

    current_value = display.get()


    # Remove the last character

    if current_value != "":

        display.delete(
            len(current_value) - 1,
            tk.END
        )


# ===========================================================
# PART 9: Clear Calculator
# ===========================================================


def clear():

    display.delete(
        0,
        tk.END
    )


# ===========================================================
# PART 10: Calculate Result
# ===========================================================


def calculate():

    expression = display.get()


    if expression == "":

        return


    # Do not calculate if expression
    # ends with an operator

    if expression[-1] in operators:

        display.delete(
            0,
            tk.END
        )

        display.insert(
            0,
            "Error"
        )

        return


    try:

        result = eval(expression)


        display.delete(
            0,
            tk.END
        )

        display.insert(
            0,
            str(result)
        )


    except ZeroDivisionError:

        display.delete(
            0,
            tk.END
        )

        display.insert(
            0,
            "Cannot divide by zero"
        )


    except:

        display.delete(
            0,
            tk.END
        )

        display.insert(
            0,
            "Error"
        )


# ===========================================================
# PART 11: Buttons Frame
# ===========================================================


buttons_frame = tk.Frame(window)

buttons_frame.pack(
    padx=20,
    pady=10,
    fill="both",
    expand=True
)


# ===========================================================
# PART 12: Configure Grid
# ===========================================================


for row in range(5):

    buttons_frame.rowconfigure(
        row,
        weight=1
    )


for column in range(4):

    buttons_frame.columnconfigure(
        column,
        weight=1
    )


# ===========================================================
# PART 13: First Row
# ===========================================================


clear_button = tk.Button(
    buttons_frame,
    text="C",
    font=("Arial", 18),
    command=clear
)

clear_button.grid(
    row=0,
    column=0,
    sticky="nsew",
    padx=3,
    pady=3
)


delete_button = tk.Button(
    buttons_frame,
    text="⌫",
    font=("Arial", 18),
    command=delete_last
)

delete_button.grid(
    row=0,
    column=1,
    sticky="nsew",
    padx=3,
    pady=3
)


divide_button = tk.Button(
    buttons_frame,
    text="/",
    font=("Arial", 18),
    command=lambda: add_operator("/")
)

divide_button.grid(
    row=0,
    column=2,
    sticky="nsew",
    padx=3,
    pady=3
)


multiply_button = tk.Button(
    buttons_frame,
    text="*",
    font=("Arial", 18),
    command=lambda: add_operator("*")
)

multiply_button.grid(
    row=0,
    column=3,
    sticky="nsew",
    padx=3,
    pady=3
)


# ===========================================================
# PART 14: Second Row
# ===========================================================


button_7 = tk.Button(
    buttons_frame,
    text="7",
    font=("Arial", 18),
    command=lambda: add_number("7")
)

button_7.grid(
    row=1,
    column=0,
    sticky="nsew",
    padx=3,
    pady=3
)


button_8 = tk.Button(
    buttons_frame,
    text="8",
    font=("Arial", 18),
    command=lambda: add_number("8")
)

button_8.grid(
    row=1,
    column=1,
    sticky="nsew",
    padx=3,
    pady=3
)


button_9 = tk.Button(
    buttons_frame,
    text="9",
    font=("Arial", 18),
    command=lambda: add_number("9")
)

button_9.grid(
    row=1,
    column=2,
    sticky="nsew",
    padx=3,
    pady=3
)


subtract_button = tk.Button(
    buttons_frame,
    text="-",
    font=("Arial", 18),
    command=lambda: add_operator("-")
)

subtract_button.grid(
    row=1,
    column=3,
    sticky="nsew",
    padx=3,
    pady=3
)


# ===========================================================
# PART 15: Third Row
# ===========================================================


button_4 = tk.Button(
    buttons_frame,
    text="4",
    font=("Arial", 18),
    command=lambda: add_number("4")
)

button_4.grid(
    row=2,
    column=0,
    sticky="nsew",
    padx=3,
    pady=3
)


button_5 = tk.Button(
    buttons_frame,
    text="5",
    font=("Arial", 18),
    command=lambda: add_number("5")
)

button_5.grid(
    row=2,
    column=1,
    sticky="nsew",
    padx=3,
    pady=3
)


button_6 = tk.Button(
    buttons_frame,
    text="6",
    font=("Arial", 18),
    command=lambda: add_number("6")
)

button_6.grid(
    row=2,
    column=2,
    sticky="nsew",
    padx=3,
    pady=3
)


add_button = tk.Button(
    buttons_frame,
    text="+",
    font=("Arial", 18),
    command=lambda: add_operator("+")
)

add_button.grid(
    row=2,
    column=3,
    sticky="nsew",
    padx=3,
    pady=3
)


# ===========================================================
# PART 16: Fourth Row
# ===========================================================


button_1 = tk.Button(
    buttons_frame,
    text="1",
    font=("Arial", 18),
    command=lambda: add_number("1")
)

button_1.grid(
    row=3,
    column=0,
    sticky="nsew",
    padx=3,
    pady=3
)


button_2 = tk.Button(
    buttons_frame,
    text="2",
    font=("Arial", 18),
    command=lambda: add_number("2")
)

button_2.grid(
    row=3,
    column=1,
    sticky="nsew",
    padx=3,
    pady=3
)


button_3 = tk.Button(
    buttons_frame,
    text="3",
    font=("Arial", 18),
    command=lambda: add_number("3")
)

button_3.grid(
    row=3,
    column=2,
    sticky="nsew",
    padx=3,
    pady=3
)


equal_button = tk.Button(
    buttons_frame,
    text="=",
    font=("Arial", 18),
    command=calculate
)

equal_button.grid(
    row=3,
    column=3,
    rowspan=2,
    sticky="nsew",
    padx=3,
    pady=3
)


# ===========================================================
# PART 17: Fifth Row
# ===========================================================


button_0 = tk.Button(
    buttons_frame,
    text="0",
    font=("Arial", 18),
    command=lambda: add_number("0")
)

button_0.grid(
    row=4,
    column=0,
    columnspan=2,
    sticky="nsew",
    padx=3,
    pady=3
)


decimal_button = tk.Button(
    buttons_frame,
    text=".",
    font=("Arial", 18),
    command=add_decimal
)

decimal_button.grid(
    row=4,
    column=2,
    sticky="nsew",
    padx=3,
    pady=3
)


# ===========================================================
# PART 18: Run Application
# ===========================================================


window.mainloop()


###########################################################
# END OF TKINTER CALCULATOR
###########################################################
