import tkinter as tk

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return "Error"

def on_button_click(symbol):
    current_text = display_var.get()
    new_text = current_text + str(symbol)
    display_var.set(new_text)

def on_clear():
    display_var.set("")

def on_equals():
    current_text = display_var.get()
    result = evaluate_expression(current_text)
    display_var.set(result)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Display
display_var = tk.StringVar()
display_entry = tk.Entry(root, textvariable=display_var, font=("Helvetica", 24), bd=10, insertwidth=2, width=14, borderwidth=4)
display_entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    '0', '.', '=', '+', 
    'C'
]

row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: on_button_click(x)
    if button == "=":
        action = on_equals
    elif button == "C":
        action = on_clear
    
    tk.Button(root, text=button, padx=20, pady=20, font=("Helvetica", 20), command=action).grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the application
root.mainloop()
