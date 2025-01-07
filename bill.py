import tkinter as tk
from tkinter import messagebox, ttk

class BillingSoftware:
    def __init__(self, root):
        self.root = root
        self.root.title("Professional Billing Software")

        # Frame for item entry
        self.frame1 = tk.Frame(root)
        self.frame1.pack(pady=10)

        tk.Label(self.frame1, text="Item Name").grid(row=0, column=0)
        self.item_name_entry = tk.Entry(self.frame1)
        self.item_name_entry.grid(row=0, column=1)

        tk.Label(self.frame1, text="Quantity").grid(row=1, column=0)
        self.quantity_entry = tk.Entry(self.frame1)
        self.quantity_entry.grid(row=1, column=1)

        tk.Label(self.frame1, text="Price per Unit").grid(row=2, column=0)
        self.price_entry = tk.Entry(self.frame1)
        self.price_entry.grid(row=2, column=1)

        tk.Label(self.frame1, text="Tax %").grid(row=3, column=0)
        self.tax_entry = tk.Entry(self.frame1)
        self.tax_entry.grid(row=3, column=1)

        self.add_button = tk.Button(self.frame1, text="Add Item", command=self.add_item)
        self.add_button.grid(row=4, columnspan=2)

        # Treeview for displaying items
        self.tree = ttk.Treeview(root, columns=("Item", "Quantity", "Price", "Tax", "Total"), show='headings')
        self.tree.heading("Item", text="Item")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Price", text="Price per Unit")
        self.tree.heading("Tax", text="Tax %")
        self.tree.heading("Total", text="Total")
        self.tree.pack(pady=10)

        # Frame for totals and buttons
        self.frame2 = tk.Frame(root)
        self.frame2.pack(pady=10)

        tk.Label(self.frame2, text="Total Amount").grid(row=0, column=0)
        self.total_var = tk.StringVar()
        self.total_label = tk.Label(self.frame2, textvariable=self.total_var)
        self.total_label.grid(row=0, column=1)

        self.calculate_button = tk.Button(self.frame2, text="Calculate Total", command=self.calculate_total)
        self.calculate_button.grid(row=1, column=0)

        self.generate_button = tk.Button(self.frame2, text="Generate Receipt", command=self.generate_receipt)
        self.generate_button.grid(row=1, column=1)

        self.items = []

    def add_item(self):
        item_name = self.item_name_entry.get()
        quantity = int(self.quantity_entry.get())
        price = float(self.price_entry.get())
        tax = float(self.tax_entry.get())

        if not item_name or not quantity or not price or not tax:
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        total = quantity * price * (1 + tax / 100)
        self.items.append((item_name, quantity, price, tax, total))
        self.update_treeview()

        self.item_name_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.tax_entry.delete(0, tk.END)

    def update_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for item in self.items:
            self.tree.insert("", "end", values=item)

    def calculate_total(self):
        total = sum(item[4] for item in self.items)
        self.total_var.set(f"{total:.2f}")

    def generate_receipt(self):
        if not self.items:
            messagebox.showwarning("Data Error", "No items to display!")
            return

        receipt = "Receipt\n\n"
        receipt += "Item\tQty\tPrice\tTax\tTotal\n"
        receipt += "-" * 40 + "\n"
        for item in self.items:
            receipt += f"{item[0]}\t{item[1]}\t{item[2]:.2f}\t{item[3]:.2f}\t{item[4]:.2f}\n"
        receipt += "-" * 40 + "\n"
        receipt += f"Total Amount: {self.total_var.get()}"

        receipt_window = tk.Toplevel(self.root)
        receipt_window.title("Receipt")
        receipt_text = tk.Text(receipt_window, wrap='word')
        receipt_text.insert(tk.END, receipt)
        receipt_text.pack(fill='both', expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = BillingSoftware(root)
    root.mainloop()
