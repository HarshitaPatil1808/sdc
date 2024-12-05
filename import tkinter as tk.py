import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

class InventoryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1000x600")

        # Title
        title = tk.Label(self.root, text="Inventory Management System", font=("Arial", 20, "bold"), bg="navy", fg="white")
        title.pack(side=tk.TOP, fill=tk.X)

        # Date and Time
        self.date_time_label = tk.Label(self.root, font=("Arial", 12), bg="navy", fg="white")
        self.date_time_label.pack(side=tk.TOP, fill=tk.X)
        self.update_time()

        # Logout Button
        logout_btn = tk.Button(self.root, text="Logout", font=("Arial", 12, "bold"), bg="yellow", fg="black", command=self.logout)
        logout_btn.place(x=900, y=30)

        # Menu
        menu_frame = tk.Frame(self.root, bd=4, relief=tk.RIDGE, bg="lightgray")
        menu_frame.place(x=0, y=70, width=200, height=530)

        menu_title = tk.Label(menu_frame, text="Menu", font=("Arial", 15, "bold"), bg="green", fg="white")
        menu_title.pack(side=tk.TOP, fill=tk.X)

        employee_btn = tk.Button(menu_frame, text="Employee", font=("Arial", 12, "bold"), bg="white", fg="black")
        employee_btn.pack(side=tk.TOP, fill=tk.X)

        supplier_btn = tk.Button(menu_frame, text="Supplier", font=("Arial", 12, "bold"), bg="white", fg="black")
        supplier_btn.pack(side=tk.TOP, fill=tk.X)

        category_btn = tk.Button(menu_frame, text="Category", font=("Arial", 12, "bold"), bg="white", fg="black")
        category_btn.pack(side=tk.TOP, fill=tk.X)

        products_btn = tk.Button(menu_frame, text="Products", font=("Arial", 12, "bold"), bg="white", fg="black")
        products_btn.pack(side=tk.TOP, fill=tk.X)

        sales_btn = tk.Button(menu_frame, text="Sales", font=("Arial", 12, "bold"), bg="white", fg="black")
        sales_btn.pack(side=tk.TOP, fill=tk.X)

        exit_btn = tk.Button(menu_frame, text="Exit", font=("Arial", 12, "bold"), bg="white", fg="black", command=self.root.quit)
        exit_btn.pack(side=tk.TOP, fill=tk.X)

        # Employee Details Frame
        details_frame = tk.Frame(self.root, bd=4, relief=tk.RIDGE, bg="white")
        details_frame.place(x=200, y=70, width=800, height=530)

        details_title = tk.Label(details_frame, text="Employee Details", font=("Arial", 15, "bold"), bg="blue", fg="white")
        details_title.grid(row=0, columnspan=4, pady=10, padx=20, sticky="w")

        # Employee Details Labels and Entries
        lbl_emp_id = tk.Label(details_frame, text="Emp ID", font=("Arial", 12, "bold"), bg="white")
        lbl_emp_id.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        txt_emp_id = tk.Entry(details_frame, font=("Arial", 12), bd=2, relief=tk.GROOVE)
        txt_emp_id.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = tk.Label(details_frame, text="Name", font=("Arial", 12, "bold"), bg="white")
        lbl_name.grid(row=1, column=2, pady=10, padx=20, sticky="w")
        txt_name = tk.Entry(details_frame, font=("Arial", 12), bd=2, relief=tk.GROOVE)
        txt_name.grid(row=1, column=3, pady=10, padx=20, sticky="w")

        lbl_email = tk.Label(details_frame, text="Email", font=("Arial", 12, "bold"), bg="white")
        lbl_email.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_email = tk.Entry(details_frame, font=("Arial", 12), bd=2, relief=tk.GROOVE)
        txt_email.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_address = tk.Label(details_frame, text="Address", font=("Arial", 12, "bold"), bg="white")
        lbl_address.grid(row=2, column=2, pady=10, padx=20, sticky="w")
        txt_address = tk.Entry(details_frame, font=("Arial", 12), bd=2, relief=tk.GROOVE)
        txt_address.grid(row=2, column=3, pady=10, padx=20, sticky="w")

        lbl_gender = tk.Label(details_frame, text="Gender", font=("Arial", 12, "bold"), bg="white")
        lbl_gender.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_gender = tk.Entry(details_frame, font=("Arial", 12), bd=2, relief=tk.GROOVE)
        txt_gender.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_dob = tk.Label(details_frame, text="D.O.B.", font=("Arial", 12, "bold"), bg="white")
        lbl_dob.grid(row=3, column=2, pady=10, padx=20, sticky="w")
        txt_dob = tk.Entry(details_frame, font=("Arial", 12), bd=2, relief=tk.GROOVE)
        txt_dob.grid(row=3, column=3, pady=10, padx=20, sticky="w")

        lbl_contact = tk.Label(details_frame, text="Contact", font=("Arial", 12, "bold"), bg="white")
        lbl_contact.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        txt_contact = tk.Entry(details_frame, font=("Arial", 12), bd=2, relief=tk.GROOVE)
        txt_contact.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        lbl_doj = tk.Label(details_frame, text="D.O.J.", font=("Arial", 12, "bold"), bg="white")
        lbl_doj.grid(row=4, column=2, pady=10, padx=20, sticky="w")
        txt_doj = tk.Entry(details_frame, font=("Arial", 12), bd=2, relief=tk.GROOVE)
        txt_doj.grid(row=4, column=3, pady=10, padx=20, sticky="w")

        lbl_password = tk.Label(details_frame, text="Password", font=("Arial", 12, "bold"), bg="white")
        lbl_password.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        txt_password = tk.Entry(details_frame, font=("Arial", 12), bd=2, relief=tk.GROOVE)
        txt_password.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_user_type = tk.Label(details_frame, text="User Type", font=("Arial", 12, "bold"), bg="white")
        lbl_user_type.grid(row=5, column=2, pady=10, padx=20, sticky="w")
        txt_user_type = tk.Entry(details_frame, font=("Arial", 12), bd=2, relief=tk.GROOVE)
        txt_user_type.grid(row=5, column=3, pady=10, padx=20, sticky="w")

        lbl_salary = tk.Label(details_frame, text="Salary", font=("Arial", 12, "bold"), bg="white")
        lbl_salary.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        txt_salary = tk.Entry(details_frame, font=("Arial", 12), bd=2, relief=tk.GROOVE)
        txt_salary.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        # Buttons for saving, updating, deleting, and clearing the employee details
        btn_save = tk.Button(details_frame, text="Save", font=("Arial", 12, "bold"), bg="green", fg="white", command=self.save_employee)
        btn_save.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        btn_update = tk.Button(details_frame, text="Update", font=("Arial", 12, "bold"), bg="blue", fg="white", command=self.update_employee)
        btn_update.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        btn_delete = tk.Button(details_frame, text="Delete", font=("Arial", 12, "bold"), bg="red", fg="white", command=self.delete_employee)
        btn_delete.grid(row=7, column=2, pady=10, padx=20, sticky="