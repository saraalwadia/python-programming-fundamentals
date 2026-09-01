###########################################################
# Tkinter Student Management System
###########################################################


import tkinter as tk
from tkinter import messagebox


# ===========================================================
# PART 1: Create Main Window
# ===========================================================


window = tk.Tk()

window.title("Student Management System")

window.geometry("900x600")

window.resizable(False, False)


# ===========================================================
# PART 2: Students Data
# ===========================================================


students = {}


# ===========================================================
# PART 3: Functions
# ===========================================================


def clear_fields():

    name_entry.delete(0, tk.END)

    id_entry.delete(0, tk.END)

    age_entry.delete(0, tk.END)

    major_entry.delete(0, tk.END)

    gpa_entry.delete(0, tk.END)


def update_students_list():

    students_listbox.delete(0, tk.END)

    for student_id, student in students.items():

        students_listbox.insert(
            tk.END,
            f"ID: {student_id} | "
            f"Name: {student['name']} | "
            f"Age: {student['age']} | "
            f"Major: {student['major']} | "
            f"GPA: {student['gpa']}"
        )

    count_label.config(
        text=f"Total Students: {len(students)}"
    )


def add_student():

    name = name_entry.get().strip()

    student_id = id_entry.get().strip()

    age = age_entry.get().strip()

    major = major_entry.get().strip()

    gpa = gpa_entry.get().strip()


    if name == "" or student_id == "" or age == "" or major == "" or gpa == "":

        messagebox.showerror(
            "Error",
            "Please fill in all fields"
        )

        return


    if student_id in students:

        messagebox.showerror(
            "Error",
            "Student ID already exists"
        )

        return


    try:

        age = int(age)

        gpa = float(gpa)


    except ValueError:

        messagebox.showerror(
            "Error",
            "Age must be a number and GPA must be numeric"
        )

        return


    if age <= 0:

        messagebox.showerror(
            "Error",
            "Age must be greater than zero"
        )

        return


    if gpa < 0 or gpa > 100:

        messagebox.showerror(
            "Error",
            "GPA must be between 0 and 100"
        )

        return


    students[student_id] = {

        "name": name,

        "age": age,

        "major": major,

        "gpa": gpa

    }


    update_students_list()

    clear_fields()


    messagebox.showinfo(
        "Success",
        "Student added successfully"
    )


def search_student():

    student_id = id_entry.get().strip()


    if student_id == "":

        messagebox.showerror(
            "Error",
            "Enter Student ID to search"
        )

        return


    if student_id in students:

        student = students[student_id]


        name_entry.delete(0, tk.END)

        name_entry.insert(
            0,
            student["name"]
        )


        age_entry.delete(0, tk.END)

        age_entry.insert(
            0,
            student["age"]
        )


        major_entry.delete(0, tk.END)

        major_entry.insert(
            0,
            student["major"]
        )


        gpa_entry.delete(0, tk.END)

        gpa_entry.insert(
            0,
            student["gpa"]
        )


        messagebox.showinfo(
            "Found",
            "Student found successfully"
        )


    else:

        messagebox.showerror(
            "Not Found",
            "Student does not exist"
        )


def update_student():

    student_id = id_entry.get().strip()


    if student_id not in students:

        messagebox.showerror(
            "Error",
            "Student ID does not exist"
        )

        return


    name = name_entry.get().strip()

    age = age_entry.get().strip()

    major = major_entry.get().strip()

    gpa = gpa_entry.get().strip()


    if name == "" or age == "" or major == "" or gpa == "":

        messagebox.showerror(
            "Error",
            "Please fill in all fields"
        )

        return


    try:

        age = int(age)

        gpa = float(gpa)


    except ValueError:

        messagebox.showerror(
            "Error",
            "Age and GPA must be valid numbers"
        )

        return


    if age <= 0:

        messagebox.showerror(
            "Error",
            "Age must be greater than zero"
        )

        return


    if gpa < 0 or gpa > 100:

        messagebox.showerror(
            "Error",
            "GPA must be between 0 and 100"
        )

        return


    students[student_id] = {

        "name": name,

        "age": age,

        "major": major,

        "gpa": gpa

    }


    update_students_list()

    clear_fields()


    messagebox.showinfo(
        "Success",
        "Student updated successfully"
    )


def delete_student():

    student_id = id_entry.get().strip()


    if student_id == "":

        messagebox.showerror(
            "Error",
            "Enter Student ID"
        )

        return


    if student_id in students:

        answer = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this student?"
        )


        if answer:

            del students[student_id]

            update_students_list()

            clear_fields()


            messagebox.showinfo(
                "Success",
                "Student deleted successfully"
            )


    else:

        messagebox.showerror(
            "Error",
            "Student does not exist"
        )


def select_student(event):

    selected = students_listbox.curselection()


    if not selected:

        return


    index = selected[0]


    student_id = list(students.keys())[index]


    student = students[student_id]


    clear_fields()


    id_entry.insert(
        0,
        student_id
    )


    name_entry.insert(
        0,
        student["name"]
    )


    age_entry.insert(
        0,
        student["age"]
    )


    major_entry.insert(
        0,
        student["major"]
    )


    gpa_entry.insert(
        0,
        student["gpa"]
    )


# ===========================================================
# PART 4: Title
# ===========================================================


title_label = tk.Label(

    window,

    text="STUDENT MANAGEMENT SYSTEM",

    font=("Arial", 22, "bold")

)


title_label.pack(

    pady=20

)


# ===========================================================
# PART 5: Main Frame
# ===========================================================


main_frame = tk.Frame(window)


main_frame.pack(

    fill="both",

    expand=True,

    padx=30

)


# ===========================================================
# PART 6: Left Frame - Student Form
# ===========================================================


form_frame = tk.Frame(main_frame)


form_frame.pack(

    side="left",

    fill="y",

    padx=20

)


# Student ID


id_label = tk.Label(

    form_frame,

    text="Student ID",

    font=("Arial", 12)

)


id_label.pack(

    anchor="w"

)


id_entry = tk.Entry(

    form_frame,

    width=30,

    font=("Arial", 12)

)


id_entry.pack(

    pady=5

)


# Student Name


name_label = tk.Label(

    form_frame,

    text="Student Name",

    font=("Arial", 12)

)


name_label.pack(

    anchor="w"

)


name_entry = tk.Entry(

    form_frame,

    width=30,

    font=("Arial", 12)

)


name_entry.pack(

    pady=5

)


# Age


age_label = tk.Label(

    form_frame,

    text="Age",

    font=("Arial", 12)

)


age_label.pack(

    anchor="w"

)


age_entry = tk.Entry(

    form_frame,

    width=30,

    font=("Arial", 12)

)


age_entry.pack(

    pady=5

)


# Major


major_label = tk.Label(

    form_frame,

    text="Major",

    font=("Arial", 12)

)


major_label.pack(

    anchor="w"

)


major_entry = tk.Entry(

    form_frame,

    width=30,

    font=("Arial", 12)

)


major_entry.pack(

    pady=5

)


# GPA


gpa_label = tk.Label(

    form_frame,

    text="GPA (0 - 100)",

    font=("Arial", 12)

)


gpa_label.pack(

    anchor="w"

)


gpa_entry = tk.Entry(

    form_frame,

    width=30,

    font=("Arial", 12)

)


gpa_entry.pack(

    pady=5

)


# ===========================================================
# PART 7: Buttons
# ===========================================================


buttons_frame = tk.Frame(

    form_frame

)


buttons_frame.pack(

    pady=15

)


add_button = tk.Button(

    buttons_frame,

    text="Add",

    width=12,

    command=add_student

)


add_button.grid(

    row=0,

    column=0,

    padx=5,

    pady=5

)


search_button = tk.Button(

    buttons_frame,

    text="Search",

    width=12,

    command=search_student

)


search_button.grid(

    row=0,

    column=1,

    padx=5,

    pady=5

)


update_button = tk.Button(

    buttons_frame,

    text="Update",

    width=12,

    command=update_student

)


update_button.grid(

    row=1,

    column=0,

    padx=5,

    pady=5

)


delete_button = tk.Button(

    buttons_frame,

    text="Delete",

    width=12,

    command=delete_student

)


delete_button.grid(

    row=1,

    column=1,

    padx=5,

    pady=5

)


clear_button = tk.Button(

    buttons_frame,

    text="Clear Fields",

    width=27,

    command=clear_fields

)


clear_button.grid(

    row=2,

    column=0,

    columnspan=2,

    padx=5,

    pady=5

)


# ===========================================================
# PART 8: Right Frame - Students List
# ===========================================================


list_frame = tk.Frame(main_frame)


list_frame.pack(

    side="right",

    fill="both",

    expand=True,

    padx=20

)


list_title = tk.Label(

    list_frame,

    text="Students List",

    font=("Arial", 14, "bold")

)


list_title.pack(

    pady=5

)


students_listbox = tk.Listbox(

    list_frame,

    width=60,

    height=20,

    font=("Arial", 10)

)


students_listbox.pack(

    fill="both",

    expand=True

)


students_listbox.bind(

    "<<ListboxSelect>>",

    select_student

)


# ===========================================================
# PART 9: Students Counter
# ===========================================================


count_label = tk.Label(

    window,

    text="Total Students: 0",

    font=("Arial", 12, "bold")

)


count_label.pack(

    pady=15

)


# ===========================================================
# PART 10: Run Application
# ===========================================================


window.mainloop()


###########################################################
# END OF STUDENT MANAGEMENT SYSTEM
###########################################################