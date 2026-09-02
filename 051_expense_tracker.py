import tkinter as tk
from tkinter import ttk, messagebox


# -------------------------
# Window Settings
# -------------------------

window = tk.Tk()
window.title("Expense Tracker")
window.geometry("700x600")
window.config(bg="#22223b")
window.resizable(False, False)


# -------------------------
# Variables
# -------------------------

expenses = []


# -------------------------
# Title
# -------------------------

title_label = tk.Label(
    window,
    text="💰 Expense Tracker",
    font=("Arial", 28, "bold"),
    bg="#22223b",
    fg="white"
)

title_label.pack(pady=20)


# -------------------------
# Input Frame
# -------------------------

input_frame = tk.Frame(
    window,
    bg="#22223b"
)

input_frame.pack(pady=10)


# -------------------------
# Description
# -------------------------

description_label = tk.Label(
    input_frame,
    text="Description:",
    font=("Arial", 12, "bold"),
    bg="#22223b",
    fg="white"
)

description_label.grid(
    row=0,
    column=0,
    padx=10,
    pady=8
)

description_entry = tk.Entry(
    input_frame,
    font=("Arial", 12),
    width=25
)

description_entry.grid(
    row=0,
    column=1,
    padx=10,
    pady=8
)


# -------------------------
# Amount
# -------------------------

amount_label = tk.Label(
    input_frame,
    text="Amount:",
    font=("Arial", 12, "bold"),
    bg="#22223b",
    fg="white"
)

amount_label.grid(
    row=1,
    column=0,
    padx=10,
    pady=8
)

amount_entry = tk.Entry(
    input_frame,
    font=("Arial", 12),
    width=25
)

amount_entry.grid(
    row=1,
    column=1,
    padx=10,
    pady=8
)


# -------------------------
# Category
# -------------------------

category_label = tk.Label(
    input_frame,
    text="Category:",
    font=("Arial", 12, "bold"),
    bg="#22223b",
    fg="white"
)

category_label.grid(
    row=2,
    column=0,
    padx=10,
    pady=8
)

category_combo = ttk.Combobox(
    input_frame,
    values=[
        "Food",
        "Transport",
        "Shopping",
        "Bills",
        "Entertainment",
        "Other"
    ],
    font=("Arial", 12),
    width=23,
    state="readonly"
)

category_combo.grid(
    row=2,
    column=1,
    padx=10,
    pady=8
)

category_combo.set("Food")


# -------------------------
# Add Expense
# -------------------------

def add_expense():

    description = description_entry.get()
    amount = amount_entry.get()
    category = category_combo.get()

    # Check description
    if description == "":
        messagebox.showwarning(
            "Missing Information",
            "Please enter a description."
        )
        return

    # Check amount
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showwarning(
            "Invalid Amount",
            "Please enter a valid number."
        )
        return

    # Check positive amount
    if amount <= 0:
        messagebox.showwarning(
            "Invalid Amount",
            "Amount must be greater than 0."
        )
        return

    # Create expense
    expense = {
        "description": description,
        "amount": amount,
        "category": category
    }

    # Add expense to list
    expenses.append(expense)

    # Add expense to table
    expense_table.insert(
        "",
        tk.END,
        values=(
            description,
            f"${amount:.2f}",
            category
        )
    )

    # Update total
    update_total()

    # Clear inputs
    description_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_combo.set("Food")


# -------------------------
# Delete Expense
# -------------------------

def delete_expense():

    selected_item = expense_table.selection()

    if not selected_item:
        messagebox.showwarning(
            "No Selection",
            "Please select an expense to delete."
        )
        return

    # Get selected item
    item = selected_item[0]

    # Get item index
    index = expense_table.index(item)

    # Delete from list
    expenses.pop(index)

    # Delete from table
    expense_table.delete(item)

    # Update total
    update_total()


# -------------------------
# Clear All Expenses
# -------------------------

def clear_expenses():

    if not expenses:
        return

    answer = messagebox.askyesno(
        "Clear Expenses",
        "Are you sure you want to delete all expenses?"
    )

    if answer:

        expenses.clear()

        for item in expense_table.get_children():
            expense_table.delete(item)

        update_total()


# -------------------------
# Update Total
# -------------------------

def update_total():

    total = 0

    for expense in expenses:
        total += expense["amount"]

    total_label.config(
        text=f"Total Expenses: ${total:.2f}"
    )


# -------------------------
# Buttons Frame
# -------------------------

button_frame = tk.Frame(
    window,
    bg="#22223b"
)

button_frame.pack(pady=15)


# -------------------------
# Add Button
# -------------------------

add_button = tk.Button(
    button_frame,
    text="➕ Add Expense",
    font=("Arial", 11, "bold"),
    bg="#06d6a0",
    fg="white",
    activebackground="#05b88a",
    relief="flat",
    width=16,
    pady=8,
    command=add_expense
)

add_button.grid(
    row=0,
    column=0,
    padx=5
)


# -------------------------
# Delete Button
# -------------------------

delete_button = tk.Button(
    button_frame,
    text="🗑️ Delete",
    font=("Arial", 11, "bold"),
    bg="#ef476f",
    fg="white",
    activebackground="#d9365e",
    relief="flat",
    width=16,
    pady=8,
    command=delete_expense
)

delete_button.grid(
    row=0,
    column=1,
    padx=5
)


# -------------------------
# Clear Button
# -------------------------

clear_button = tk.Button(
    button_frame,
    text="🧹 Clear All",
    font=("Arial", 11, "bold"),
    bg="#118ab2",
    fg="white",
    activebackground="#0d6f91",
    relief="flat",
    width=16,
    pady=8,
    command=clear_expenses
)

clear_button.grid(
    row=0,
    column=2,
    padx=5
)


# -------------------------
# Expense Table
# -------------------------

table_frame = tk.Frame(
    window,
    bg="#22223b"
)

table_frame.pack(
    padx=30,
    pady=10
)


expense_table = ttk.Treeview(
    table_frame,
    columns=(
        "Description",
        "Amount",
        "Category"
    ),
    show="headings",
    height=8
)


expense_table.heading(
    "Description",
    text="Description"
)

expense_table.heading(
    "Amount",
    text="Amount"
)

expense_table.heading(
    "Category",
    text="Category"
)


expense_table.column(
    "Description",
    width=250
)

expense_table.column(
    "Amount",
    width=150,
    anchor="center"
)

expense_table.column(
    "Category",
    width=150,
    anchor="center"
)


expense_table.pack()


# -------------------------
# Total
# -------------------------

total_label = tk.Label(
    window,
    text="Total Expenses: $0.00",
    font=("Arial", 18, "bold"),
    bg="#22223b",
    fg="#ffd166"
)

total_label.pack(pady=15)


# -------------------------
# Start Application
# -------------------------

window.mainloop()