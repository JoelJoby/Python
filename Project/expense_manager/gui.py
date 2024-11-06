# gui.py
import tkinter as tk
from tkinter import messagebox

def add_expense_gui():
    window = tk.Tk()
    window.title("Add Expense")
    
    # Add widgets for input fields (e.g., title, amount, category)
    title_label = tk.Label(window, text="Expense Title:")
    title_label.pack()
    title_entry = tk.Entry(window)
    title_entry.pack()

    # Add other necessary fields like amount, category, etc.
    # Save the expense logic here

    window.mainloop()

def view_expenses_gui(root):  # Accept 'root' as a parameter
    window = tk.Toplevel(root)  # Use Toplevel if you want it to be a child window
    window.title("View Expenses")

    label = tk.Label(window, text="Here are your expenses:")
    label.pack()

    # Display a message or your list of expenses
    messagebox.showinfo("Expense List", "Here are the expenses...")

    window.mainloop()

def delete_expense_gui():
    # Your code to delete an expense
    pass

def generate_report():
    # Your code to generate a report
    pass
