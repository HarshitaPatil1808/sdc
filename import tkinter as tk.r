import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("Inventory Management System")
root.geometry("1024x600")

# Header
header_frame = tk.Frame(root, bg="navy", height=80)
header_frame.pack(fill=tk.X)

header_label = tk.Label(header_frame, text="Inventory Management System", fg="white", bg="navy", font=("Arial", 24))
header_label.pack(pady=10)

welcome_label = tk.Label(header_frame, text="Welcome to Inventory Management System", fg="white", bg="navy", font=("Arial", 12))
welcome_label.pack()

# Logout Button
logout_btn = tk.Button(header_frame, text="Logout", bg="yellow", fg="black", font=("Arial", 12, "bold"))
logout_btn.place(x=900, y=20)

# Sidebar (Menu)
sidebar_frame = tk.Frame(root, bg="teal", width=200)
sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)

menu_items = ["Employee", "Supplier", "Category", "Products", "Sales", "Exit"]
for item in menu_items:
    btn = tk.Button(sidebar_frame, text=item, font=("Arial", 12), bg="white", fg="black", relief="flat")
    btn.pack(fill=tk.X, pady=5, padx=10)

# Employee Details Section
details_frame = tk.Frame(root, bg="white")
details_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Search Section
search_label = tk.Label(details_frame, text="Search Employee", font=("Arial", 14), bg="white")
search_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

search_field = ttk.Combobox(details_frame, width=20, values=["Emp ID", "Name", "Email"])
search_field.grid(row=0, column=1, pady=10, padx=10)

search_entry = tk.Entry(details_frame, width=30)
search_entry.grid(row=0, column=2, pady=10, padx=10)

search_btn = tk.Button(details_frame, text="Search", bg="green", fg="white", font=("Arial", 12, "bold"))
search_btn.grid(row=0, column=3, pady=10, padx=10)

# Form Section
form_labels = ["Emp ID", "Name", "Email", "Address", "Gender", "Contact", "D.O.B.", "D.O.J.", "Password", "User Type", "Salary"]
row = 1
col = 0

for label in form_labels:
    tk.Label(details_frame, text=label, font=("Arial", 12), bg="white").grid(row=row, column=col, padx=10, pady=5, sticky="w")
    if label in ["Gender", "User Type"]:
        ttk.Combobox(details_frame, width=20).grid(row=row, column=col + 1, padx=10, pady=5)
    else:
        tk.Entry(details_frame, width=30).grid(row=row, column=col + 1, padx=10, pady=5)
    row += 1
    if row > 4:
        row = 1
        col += 2

# Action Buttons
action_frame = tk.Frame(details_frame, bg="white")
action_frame.grid(row=6, column=0, columnspan=4, pady=10)

actions = [("Save", "blue"), ("Update", "green"), ("Delete", "red"), ("Clear", "gray")]
for text, color in actions:
    btn = tk.Button(action_frame, text=text, bg=color, fg="white", font=("Arial", 12, "bold"))
    btn.pack(side=tk.LEFT, padx=10)

# Employee Table (Dummy Data)
table_frame = tk.Frame(details_frame)
table_frame.grid(row=7, column=0, columnspan=4, pady=20)

columns = ["EMP ID", "Name", "Email", "Gender", "Contact", "D.O.B.", "D.O.J.", "Password", "User Type", "Address", "Salary"]
table = ttk.Treeview(table_frame, columns=columns, show="headings", height=8)

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=100)

table.pack(fill=tk.X)

# Run the GUI
root.mainloop()
