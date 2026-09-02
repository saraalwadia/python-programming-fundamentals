###########################################################
# Business Management System
# Final Project - Python Programming Fundamentals
###########################################################

import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime
import os


# ===========================================================
# PART 1: Database Settings
# ===========================================================

DATABASE_FOLDER = "053_business_management_system"
DATABASE_NAME = os.path.join(DATABASE_FOLDER, "business.db")

# ===========================================================
# PART 2: Connect to Database
# ===========================================================

def connect_db():
    return sqlite3.connect(DATABASE_NAME)


# ===========================================================
# PART 3: Create Database
# ===========================================================

def create_database():

    connection = connect_db()
    cursor = connection.cursor()

    # Products table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
    """)

    # Sales table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            total REAL NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
    """)

    connection.commit()
    connection.close()


# ===========================================================
# PART 4: Main Window
# ===========================================================

root = tk.Tk()

root.title("Business Management System")
root.geometry("1100x700")
root.minsize(950, 600)


# ===========================================================
# PART 5: Variables
# ===========================================================

product_name_var = tk.StringVar()
category_var = tk.StringVar()
price_var = tk.StringVar()
quantity_var = tk.StringVar()

search_var = tk.StringVar()

sale_product_var = tk.StringVar()
sale_quantity_var = tk.StringVar()


# ===========================================================
# PART 6: Product Functions
# ===========================================================

def clear_product_fields():

    product_name_var.set("")
    category_var.set("")
    price_var.set("")
    quantity_var.set("")


# ===========================================================
# PART 7: Refresh Products
# ===========================================================

def refresh_products():

    # Clear table
    for item in product_tree.get_children():
        product_tree.delete(item)

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, category, price, quantity
        FROM products
        ORDER BY id DESC
    """)

    products = cursor.fetchall()

    for product in products:

        product_tree.insert(
            "",
            tk.END,
            values=(
                product[0],
                product[1],
                product[2],
                f"${product[3]:.2f}",
                product[4]
            )
        )

    connection.close()

    # Update other parts of the application
    update_dashboard()
    load_products_for_sales()


# ===========================================================
# PART 8: Add Product
# ===========================================================

def add_product():

    name = product_name_var.get().strip()
    category = category_var.get().strip()
    price = price_var.get().strip()
    quantity = quantity_var.get().strip()

    if not name or not category or not price or not quantity:

        messagebox.showwarning(
            "Missing Data",
            "Please fill in all fields."
        )

        return

    try:

        price = float(price)
        quantity = int(quantity)

        if price < 0 or quantity < 0:
            raise ValueError

    except ValueError:

        messagebox.showerror(
            "Invalid Data",
            "Price must be a positive number and quantity must be an integer."
        )

        return

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO products
        (name, category, price, quantity)
        VALUES (?, ?, ?, ?)
    """, (
        name,
        category,
        price,
        quantity
    ))

    connection.commit()
    connection.close()

    messagebox.showinfo(
        "Success",
        "Product added successfully!"
    )

    clear_product_fields()

    # Refresh products AND Sales dropdown
    refresh_products()


# ===========================================================
# PART 9: Select Product
# ===========================================================

def select_product(event):

    selected = product_tree.selection()

    if not selected:
        return

    item = product_tree.item(selected[0])

    values = item["values"]

    product_name_var.set(values[1])
    category_var.set(values[2])
    price_var.set(
        str(values[3]).replace("$", "")
    )
    quantity_var.set(values[4])


# ===========================================================
# PART 10: Update Product
# ===========================================================

def update_product():

    selected = product_tree.selection()

    if not selected:

        messagebox.showwarning(
            "Select Product",
            "Please select a product first."
        )

        return

    item = product_tree.item(selected[0])

    product_id = item["values"][0]

    name = product_name_var.get().strip()
    category = category_var.get().strip()
    price = price_var.get().strip()
    quantity = quantity_var.get().strip()

    if not name or not category or not price or not quantity:

        messagebox.showwarning(
            "Missing Data",
            "Please fill in all fields."
        )

        return

    try:

        price = float(price)
        quantity = int(quantity)

        if price < 0 or quantity < 0:
            raise ValueError

    except ValueError:

        messagebox.showerror(
            "Invalid Data",
            "Please enter valid price and quantity."
        )

        return

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE products
        SET name = ?,
            category = ?,
            price = ?,
            quantity = ?
        WHERE id = ?
    """, (
        name,
        category,
        price,
        quantity,
        product_id
    ))

    connection.commit()
    connection.close()

    messagebox.showinfo(
        "Success",
        "Product updated successfully!"
    )

    clear_product_fields()

    refresh_products()


# ===========================================================
# PART 11: Delete Product
# ===========================================================

def delete_product():

    selected = product_tree.selection()

    if not selected:

        messagebox.showwarning(
            "Select Product",
            "Please select a product first."
        )

        return

    item = product_tree.item(selected[0])

    product_id = item["values"][0]

    # Check if product has sales
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM sales
        WHERE product_id = ?
    """, (product_id,))

    sales_count = cursor.fetchone()[0]

    if sales_count > 0:

        connection.close()

        messagebox.showwarning(
            "Cannot Delete",
            "This product has sales records and cannot be deleted."
        )

        return

    confirm = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this product?"
    )

    if not confirm:

        connection.close()

        return

    cursor.execute("""
        DELETE FROM products
        WHERE id = ?
    """, (product_id,))

    connection.commit()
    connection.close()

    messagebox.showinfo(
        "Deleted",
        "Product deleted successfully!"
    )

    clear_product_fields()

    refresh_products()


# ===========================================================
# PART 12: Search Products
# ===========================================================

def search_products():

    search_text = search_var.get().strip()

    for item in product_tree.get_children():
        product_tree.delete(item)

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, category, price, quantity
        FROM products
        WHERE name LIKE ?
        OR category LIKE ?
        ORDER BY id DESC
    """, (
        f"%{search_text}%",
        f"%{search_text}%"
    ))

    products = cursor.fetchall()

    for product in products:

        product_tree.insert(
            "",
            tk.END,
            values=(
                product[0],
                product[1],
                product[2],
                f"${product[3]:.2f}",
                product[4]
            )
        )

    connection.close()


# ===========================================================
# PART 13: Load Products for Sales
# ===========================================================

def load_products_for_sales():

    # Clear current values
    sale_product_combo["values"] = ()
    sale_product_var.set("")

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name
        FROM products
        WHERE quantity > 0
        ORDER BY name
    """)

    products = cursor.fetchall()

    # Store ID and name together
    product_values = []

    for product in products:

        product_id = product[0]
        product_name = product[1]

        product_values.append(
            f"{product_id} - {product_name}"
        )

    sale_product_combo["values"] = product_values

    connection.close()


# ===========================================================
# PART 14: Make Sale
# ===========================================================

def make_sale():

    selected_product = sale_product_var.get().strip()
    sale_quantity_text = sale_quantity_var.get().strip()

    if not selected_product or not sale_quantity_text:

        messagebox.showwarning(
            "Missing Data",
            "Please select a product and enter quantity."
        )

        return

    try:

        sale_quantity = int(sale_quantity_text)

        if sale_quantity <= 0:
            raise ValueError

    except ValueError:

        messagebox.showerror(
            "Invalid Quantity",
            "Quantity must be a positive integer."
        )

        return

    try:

        # Extract Product ID
        product_id = int(
            selected_product.split(" - ")[0]
        )

    except ValueError:

        messagebox.showerror(
            "Error",
            "Invalid product selection."
        )

        return

    connection = connect_db()
    cursor = connection.cursor()

    # Get product information
    cursor.execute("""
        SELECT name, price, quantity
        FROM products
        WHERE id = ?
    """, (product_id,))

    product = cursor.fetchone()

    if not product:

        connection.close()

        messagebox.showerror(
            "Error",
            "Product not found."
        )

        return

    product_name = product[0]
    price = product[1]
    available_quantity = product[2]

    # Check stock
    if sale_quantity > available_quantity:

        connection.close()

        messagebox.showwarning(
            "Not Enough Stock",
            f"Only {available_quantity} item(s) available."
        )

        return

    # Calculate total
    total = price * sale_quantity

    # Update stock
    new_quantity = (
        available_quantity - sale_quantity
    )

    cursor.execute("""
        UPDATE products
        SET quantity = ?
        WHERE id = ?
    """, (
        new_quantity,
        product_id
    ))

    # Current date and time
    sale_date = datetime.now().strftime(
        "%Y-%m-%d %H:%M"
    )

    # Add sale record
    cursor.execute("""
        INSERT INTO sales
        (product_id, quantity, total, date)
        VALUES (?, ?, ?, ?)
    """, (
        product_id,
        sale_quantity,
        total,
        sale_date
    ))

    connection.commit()
    connection.close()

    messagebox.showinfo(
        "Sale Completed",
        f"Sale completed successfully!\n\n"
        f"Product: {product_name}\n"
        f"Quantity: {sale_quantity}\n"
        f"Total: ${total:.2f}\n"
        f"Remaining Stock: {new_quantity}"
    )

    sale_product_var.set("")
    sale_quantity_var.set("")

    # Refresh everything
    refresh_products()
    refresh_sales()
    load_products_for_sales()


# ===========================================================
# PART 15: Refresh Sales
# ===========================================================

def refresh_sales():

    for item in sales_tree.get_children():
        sales_tree.delete(item)

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            sales.id,
            products.name,
            sales.quantity,
            sales.total,
            sales.date
        FROM sales
        INNER JOIN products
        ON sales.product_id = products.id
        ORDER BY sales.id DESC
    """)

    sales = cursor.fetchall()

    for sale in sales:

        sales_tree.insert(
            "",
            tk.END,
            values=(
                sale[0],
                sale[1],
                sale[2],
                f"${sale[3]:.2f}",
                sale[4]
            )
        )

    connection.close()


# ===========================================================
# PART 16: Dashboard
# ===========================================================

def update_dashboard():

    connection = connect_db()
    cursor = connection.cursor()

    # Number of products
    cursor.execute("""
        SELECT COUNT(*)
        FROM products
    """)

    total_products = cursor.fetchone()[0]

    # Total stock
    cursor.execute("""
        SELECT COALESCE(SUM(quantity), 0)
        FROM products
    """)

    total_stock = cursor.fetchone()[0]

    # Total sales
    cursor.execute("""
        SELECT COALESCE(SUM(total), 0)
        FROM sales
    """)

    total_sales = cursor.fetchone()[0]

    # Number of transactions
    cursor.execute("""
        SELECT COUNT(*)
        FROM sales
    """)

    total_transactions = cursor.fetchone()[0]

    connection.close()

    products_value_label.config(
        text=str(total_products)
    )

    stock_value_label.config(
        text=str(total_stock)
    )

    sales_value_label.config(
        text=f"${total_sales:.2f}"
    )

    transactions_value_label.config(
        text=str(total_transactions)
    )


# ===========================================================
# PART 17: Notebook
# ===========================================================

notebook = ttk.Notebook(root)

notebook.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)


# ===========================================================
# PART 18: Dashboard Tab
# ===========================================================

dashboard_frame = ttk.Frame(notebook)

notebook.add(
    dashboard_frame,
    text="  Dashboard  "
)


tk.Label(
    dashboard_frame,
    text="Business Management System",
    font=("Arial", 26, "bold")
).pack(pady=30)


tk.Label(
    dashboard_frame,
    text="Manage products, inventory and sales",
    font=("Arial", 13)
).pack()


cards_frame = tk.Frame(
    dashboard_frame
)

cards_frame.pack(pady=50)


# -----------------------------------------------------------
# Card 1
# -----------------------------------------------------------

card1 = tk.Frame(
    cards_frame,
    bd=1,
    relief="solid",
    width=220,
    height=130
)

card1.grid(
    row=0,
    column=0,
    padx=10
)

card1.pack_propagate(False)


tk.Label(
    card1,
    text="Total Products",
    font=("Arial", 13)
).pack(pady=15)


products_value_label = tk.Label(
    card1,
    text="0",
    font=("Arial", 25, "bold")
)

products_value_label.pack()


# -----------------------------------------------------------
# Card 2
# -----------------------------------------------------------

card2 = tk.Frame(
    cards_frame,
    bd=1,
    relief="solid",
    width=220,
    height=130
)

card2.grid(
    row=0,
    column=1,
    padx=10
)

card2.pack_propagate(False)


tk.Label(
    card2,
    text="Items in Stock",
    font=("Arial", 13)
).pack(pady=15)


stock_value_label = tk.Label(
    card2,
    text="0",
    font=("Arial", 25, "bold")
)

stock_value_label.pack()


# -----------------------------------------------------------
# Card 3
# -----------------------------------------------------------

card3 = tk.Frame(
    cards_frame,
    bd=1,
    relief="solid",
    width=220,
    height=130
)

card3.grid(
    row=0,
    column=2,
    padx=10
)

card3.pack_propagate(False)


tk.Label(
    card3,
    text="Total Sales",
    font=("Arial", 13)
).pack(pady=15)


sales_value_label = tk.Label(
    card3,
    text="$0.00",
    font=("Arial", 25, "bold")
)

sales_value_label.pack()


# -----------------------------------------------------------
# Card 4
# -----------------------------------------------------------

card4 = tk.Frame(
    cards_frame,
    bd=1,
    relief="solid",
    width=220,
    height=130
)

card4.grid(
    row=0,
    column=3,
    padx=10
)

card4.pack_propagate(False)


tk.Label(
    card4,
    text="Transactions",
    font=("Arial", 13)
).pack(pady=15)


transactions_value_label = tk.Label(
    card4,
    text="0",
    font=("Arial", 25, "bold")
)

transactions_value_label.pack()


# ===========================================================
# PART 19: Products Tab
# ===========================================================

products_frame = ttk.Frame(notebook)

notebook.add(
    products_frame,
    text="  Products  "
)


# -----------------------------------------------------------
# Product Form
# -----------------------------------------------------------

form_frame = ttk.LabelFrame(
    products_frame,
    text="Product Information"
)

form_frame.pack(
    fill="x",
    padx=15,
    pady=15
)


ttk.Label(
    form_frame,
    text="Product Name:"
).grid(
    row=0,
    column=0,
    padx=10,
    pady=10
)


ttk.Entry(
    form_frame,
    textvariable=product_name_var,
    width=25
).grid(
    row=0,
    column=1,
    padx=10,
    pady=10
)


ttk.Label(
    form_frame,
    text="Category:"
).grid(
    row=0,
    column=2,
    padx=10,
    pady=10
)


ttk.Entry(
    form_frame,
    textvariable=category_var,
    width=25
).grid(
    row=0,
    column=3,
    padx=10,
    pady=10
)


ttk.Label(
    form_frame,
    text="Price:"
).grid(
    row=1,
    column=0,
    padx=10,
    pady=10
)


ttk.Entry(
    form_frame,
    textvariable=price_var,
    width=25
).grid(
    row=1,
    column=1,
    padx=10,
    pady=10
)


ttk.Label(
    form_frame,
    text="Quantity:"
).grid(
    row=1,
    column=2,
    padx=10,
    pady=10
)


ttk.Entry(
    form_frame,
    textvariable=quantity_var,
    width=25
).grid(
    row=1,
    column=3,
    padx=10,
    pady=10
)


# -----------------------------------------------------------
# Product Buttons
# -----------------------------------------------------------

buttons_frame = ttk.Frame(
    form_frame
)

buttons_frame.grid(
    row=2,
    column=0,
    columnspan=4,
    pady=10
)


ttk.Button(
    buttons_frame,
    text="Add Product",
    command=add_product
).grid(
    row=0,
    column=0,
    padx=5
)


ttk.Button(
    buttons_frame,
    text="Update",
    command=update_product
).grid(
    row=0,
    column=1,
    padx=5
)


ttk.Button(
    buttons_frame,
    text="Delete",
    command=delete_product
).grid(
    row=0,
    column=2,
    padx=5
)


ttk.Button(
    buttons_frame,
    text="Clear",
    command=clear_product_fields
).grid(
    row=0,
    column=3,
    padx=5
)


# -----------------------------------------------------------
# Search
# -----------------------------------------------------------

search_frame = ttk.Frame(
    products_frame
)

search_frame.pack(
    fill="x",
    padx=15,
    pady=5
)


ttk.Label(
    search_frame,
    text="Search:"
).pack(
    side="left",
    padx=5
)


ttk.Entry(
    search_frame,
    textvariable=search_var,
    width=35
).pack(
    side="left",
    padx=5
)


ttk.Button(
    search_frame,
    text="Search",
    command=search_products
).pack(
    side="left",
    padx=5
)


ttk.Button(
    search_frame,
    text="Show All",
    command=refresh_products
).pack(
    side="left",
    padx=5
)


# -----------------------------------------------------------
# Product Table
# -----------------------------------------------------------

table_frame = ttk.Frame(
    products_frame
)

table_frame.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=10
)


product_tree = ttk.Treeview(
    table_frame,
    columns=(
        "ID",
        "Name",
        "Category",
        "Price",
        "Quantity"
    ),
    show="headings"
)


product_tree.heading(
    "ID",
    text="ID"
)

product_tree.heading(
    "Name",
    text="Product Name"
)

product_tree.heading(
    "Category",
    text="Category"
)

product_tree.heading(
    "Price",
    text="Price"
)

product_tree.heading(
    "Quantity",
    text="Quantity"
)


product_tree.column(
    "ID",
    width=60
)

product_tree.column(
    "Name",
    width=220
)

product_tree.column(
    "Category",
    width=180
)

product_tree.column(
    "Price",
    width=120
)

product_tree.column(
    "Quantity",
    width=120
)


product_scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=product_tree.yview
)


product_tree.configure(
    yscrollcommand=product_scrollbar.set
)


product_scrollbar.pack(
    side="right",
    fill="y"
)


product_tree.pack(
    fill="both",
    expand=True
)


product_tree.bind(
    "<ButtonRelease-1>",
    select_product
)


# ===========================================================
# PART 20: Sales Tab
# ===========================================================

sales_frame = ttk.Frame(notebook)

notebook.add(
    sales_frame,
    text="  Sales  "
)


# -----------------------------------------------------------
# Sale Form
# -----------------------------------------------------------

sale_form = ttk.LabelFrame(
    sales_frame,
    text="Create Sale"
)

sale_form.pack(
    fill="x",
    padx=15,
    pady=15
)


ttk.Label(
    sale_form,
    text="Product:"
).grid(
    row=0,
    column=0,
    padx=10,
    pady=15
)


sale_product_combo = ttk.Combobox(
    sale_form,
    textvariable=sale_product_var,
    state="readonly",
    width=30
)


sale_product_combo.grid(
    row=0,
    column=1,
    padx=10,
    pady=15
)


ttk.Label(
    sale_form,
    text="Quantity:"
).grid(
    row=0,
    column=2,
    padx=10,
    pady=15
)


ttk.Entry(
    sale_form,
    textvariable=sale_quantity_var,
    width=15
).grid(
    row=0,
    column=3,
    padx=10,
    pady=15
)


ttk.Button(
    sale_form,
    text="Complete Sale",
    command=make_sale
).grid(
    row=0,
    column=4,
    padx=10,
    pady=15
)


ttk.Button(
    sale_form,
    text="Refresh Products",
    command=load_products_for_sales
).grid(
    row=0,
    column=5,
    padx=10,
    pady=15
)


# -----------------------------------------------------------
# Sales Table
# -----------------------------------------------------------

sales_table_frame = ttk.Frame(
    sales_frame
)

sales_table_frame.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=10
)


sales_tree = ttk.Treeview(
    sales_table_frame,
    columns=(
        "ID",
        "Product",
        "Quantity",
        "Total",
        "Date"
    ),
    show="headings"
)


sales_tree.heading(
    "ID",
    text="ID"
)

sales_tree.heading(
    "Product",
    text="Product"
)

sales_tree.heading(
    "Quantity",
    text="Quantity"
)

sales_tree.heading(
    "Total",
    text="Total"
)

sales_tree.heading(
    "Date",
    text="Date"
)


sales_tree.column(
    "ID",
    width=70
)

sales_tree.column(
    "Product",
    width=250
)

sales_tree.column(
    "Quantity",
    width=120
)

sales_tree.column(
    "Total",
    width=150
)

sales_tree.column(
    "Date",
    width=200
)


sales_scrollbar = ttk.Scrollbar(
    sales_table_frame,
    orient="vertical",
    command=sales_tree.yview
)


sales_tree.configure(
    yscrollcommand=sales_scrollbar.set
)


sales_scrollbar.pack(
    side="right",
    fill="y"
)


sales_tree.pack(
    fill="both",
    expand=True
)


# ===========================================================
# PART 21: About Tab
# ===========================================================

about_frame = ttk.Frame(notebook)

notebook.add(
    about_frame,
    text="  About  "
)


tk.Label(
    about_frame,
    text="Business Management System",
    font=("Arial", 24, "bold")
).pack(
    pady=40
)


tk.Label(
    about_frame,
    text="Final Project - Python Programming Fundamentals",
    font=("Arial", 14)
).pack(
    pady=10
)


tk.Label(
    about_frame,
    text=(
        "A desktop application for managing products, "
        "inventory and sales using Python, Tkinter and SQLite."
    ),
    font=("Arial", 12),
    wraplength=700,
    justify="center"
).pack(
    pady=20
)


tk.Label(
    about_frame,
    text=(
        "Concepts used:\n\n"
        "Python Functions\n"
        "Conditional Statements\n"
        "Loops\n"
        "Exception Handling\n"
        "Tkinter GUI\n"
        "SQLite Database\n"
        "CRUD Operations\n"
        "SQL Queries\n"
        "Foreign Keys\n"
        "Data Validation"
    ),
    font=("Arial", 11),
    justify="center"
).pack(
    pady=20
)


# ===========================================================
# PART 22: Initialize Application
# ===========================================================

create_database()

refresh_products()
refresh_sales()
load_products_for_sales()
update_dashboard()


# ===========================================================
# PART 23: Start Application
# ===========================================================

root.mainloop()


###########################################################
# END OF BUSINESS MANAGEMENT SYSTEM
###########################################################