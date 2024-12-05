from tkinter import *
from tkinter import ttk

# Function for exit button
def exit_system():
    root.destroy()

# Main application window
root = Tk()
root.title("Inventory Management System")
root.geometry("1000x600")

# Top Frame
top_frame = Frame(root, bg="navy", height=70)
top_frame.pack(fill=X)

# Title
title_label = Label(
    top_frame, text="Inventory Management System", font=("Arial", 20, "bold"), bg="navy", fg="white"
)
title_label.place(x=20, y=10)

# Date & Time
date_label = Label(
    top_frame, text="Date: DD:MM:YYYY", font=("Arial", 12), bg="navy", fg="white"
)
date_label.place(x=700, y=10)

time_label = Label(
    top_frame, text="Time: HH:MM:SS", font=("Arial", 12), bg="navy", fg="white"
)
time_label.place(x=700, y=40)

# Logout Button
logout_button = Button(top_frame, text="Logout", bg="yellow", fg="black", font=("Arial", 12, "bold"), command=exit_system)
logout_button.place(x=900, y=20)

# Left Menu Frame
menu_frame = Frame(root, bg="teal", width=200)
menu_frame.pack(side=LEFT, fill=Y)

menu_title = Label(menu_frame, text="Menu", font=("Arial", 16, "bold"), bg="teal", fg="white")
menu_title.pack(pady=10)

menu_buttons = ["Employee", "Supplier", "Category", "Products", "Sales", "Exit"]
for button in menu_buttons:
    btn = Button(menu_frame, text=f"» {button}", font=("Arial", 14), width=15, bg="white", fg="black", bd=0, command=exit_system if button == "Exit" else None)
    btn.pack(pady=5)

# Dashboard Section
dashboard_frame = Frame(root, bg="white", bd=2)
dashboard_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

dashboard_title = Label(dashboard_frame, text="Welcome to Inventory Management System", font=("Arial", 16, "bold"), bg="white")
dashboard_title.pack(pady=10)

# Dashboard Data Panels
data_frame = Frame(dashboard_frame, bg="white")
data_frame.pack()

panels = [
    ("Total Employee", "cyan"),
    ("Total Supplier", "orange"),
    ("Total Category", "green"),
    ("Total Product", "gray"),
    ("Total Sales", "yellow"),
]

for panel in panels:
    frame = Frame(data_frame, bg=panel[1], width=150, height=100)
    frame.pack(side=LEFT, padx=20, pady=10)
    Label(frame, text=panel[0], font=("Arial", 14, "bold"), bg=panel[1], fg="white").pack(pady=10)
    Label(frame, text="{ 0 }", font=("Arial", 18, "bold"), bg=panel[1], fg="white").pack()
