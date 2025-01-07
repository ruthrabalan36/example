import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class FinanceManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Manager")

        # Data
        self.entries = []

        # Frames
        self.frame1 = tk.Frame(root)
        self.frame1.pack(pady=10)
        self.frame2 = tk.Frame(root)
        self.frame2.pack(pady=10)

        # Widgets for Entry
        tk.Label(self.frame1, text="Date (YYYY-MM-DD)").grid(row=0, column=0)
        self.date_entry = tk.Entry(self.frame1)
        self.date_entry.grid(row=0, column=1)

        tk.Label(self.frame1, text="Description").grid(row=1, column=0)
        self.desc_entry = tk.Entry(self.frame1)
        self.desc_entry.grid(row=1, column=1)

        tk.Label(self.frame1, text="Amount").grid(row=2, column=0)
        self.amount_entry = tk.Entry(self.frame1)
        self.amount_entry.grid(row=2, column=1)

        self.category_var = tk.StringVar(value="Income")
        tk.Label(self.frame1, text="Category").grid(row=3, column=0)
        tk.Radiobutton(self.frame1, text="Income", variable=self.category_var, value="Income").grid(row=3, column=1)
        tk.Radiobutton(self.frame1, text="Expense", variable=self.category_var, value="Expense").grid(row=3, column=2)

        self.add_button = tk.Button(self.frame1, text="Add Entry", command=self.add_entry)
        self.add_button.grid(row=4, columnspan=3)

        # Listbox for displaying entries
        self.listbox = tk.Listbox(self.frame2, width=50, height=10)
        self.listbox.pack()

        # Buttons for actions
        self.delete_button = tk.Button(self.frame2, text="Delete Entry", command=self.delete_entry)
        self.delete_button.pack(side='left', padx=10)
        self.view_chart_button = tk.Button(self.frame2, text="View Chart", command=self.view_chart)
        self.view_chart_button.pack(side='right', padx=10)

    def add_entry(self):
        date = self.date_entry.get()
        description = self.desc_entry.get()
        amount = float(self.amount_entry.get())
        category = self.category_var.get()
        
        if not date or not description or not amount:
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        entry = (date, description, amount, category)
        self.entries.append(entry)
        self.update_listbox()

        self.date_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

    def delete_entry(self):
        selected_entry_index = self.listbox.curselection()
        if selected_entry_index:
            del self.entries[selected_entry_index[0]]
            self.update_listbox()
        else:
            messagebox.showwarning("Selection Error", "No entry selected!")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for entry in self.entries:
            self.listbox.insert(tk.END, f"{entry[0]} - {entry[1]}: {entry[2]} ({entry[3]})")

    def view_chart(self):
        if not self.entries:
            messagebox.showwarning("Data Error", "No entries to display!")
            return

        income = sum(entry[2] for entry in self.entries if entry[3] == "Income")
        expense = sum(entry[2] for entry in self.entries if entry[3] == "Expense")
        labels = ["Income", "Expense"]
        values = [income, expense]

        plt.bar(labels, values, color=["green", "red"])
        plt.title("Income vs Expense")
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    manager = FinanceManager(root)
    root.mainloop()
