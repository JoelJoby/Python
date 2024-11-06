# app.py
import tkinter as tk
from tkinter import messagebox
from database import create_db, add_expense, view_expenses, delete_expense
from gui import add_expense_gui, view_expenses_gui, delete_expense_gui, generate_report

def main():
    # Initialize the GUI
    root = tk.Tk()
    root.title("Expense Tracker")

    # GUI elements (labels, entries, buttons) would go here
    # Add Expense Button
    tk.Button(root, text="Add Expense", command=lambda: add_expense_gui()).grid(row=4, column=0, columnspan=2)
    
    # Delete Expense Button
    tk.Button(root, text="Delete Expense", command=lambda: delete_expense_gui()).grid(row=6, column=0, columnspan=2)

    # Treeview to display expenses
    view_expenses_gui(root)

    # Start the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()
