import tkinter as tk
from tkinter import ttk

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

def calculate():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    selected_operations = list(operation_listbox.curselection())
    results = []

    for index in selected_operations:
        operation = operation_choices[index]
        if operation == "Add":
            results.append(add(num1, num2))
        elif operation == "Subtract":
            results.append(subtract(num1, num2))
        elif operation == "Multiply":
            results.append(multiply(num1, num2))
        elif operation == "Divide":
            results.append(divide(num1, num2))

    result_label.config(text=f"Results: {', '.join(map(str, results))}")

def reset():
    num1_entry.delete(0, tk.END)
    num2_entry.delete(0, tk.END)
    result_label.config(text="Result: ")

app = tk.Tk()
app.title("Simple Calculator")

# Number Entries
num1_label = ttk.Label(app, text="Number 1:")
num1_label.grid(row=0, column=0)
num1_entry = ttk.Entry(app)
num1_entry.grid(row=0, column=1)

num2_label = ttk.Label(app, text="Number 2:")
num2_label.grid(row=1, column=0)
num2_entry = ttk.Entry(app)
num2_entry.grid(row=1, column=1)

# Operation Listbox with Scrollbar
operation_choices = ["Add", "Subtract", "Multiply", "Divide"]
operation_listbox = tk.Listbox(app, selectmode=tk.MULTIPLE, height=len(operation_choices))
for choice in operation_choices:
    operation_listbox.insert(tk.END, choice)
operation_listbox.grid(row=2, column=0, columnspan=2)

# Calculate Button
calculate_button = ttk.Button(app, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2)

# Reset Button
reset_button = ttk.Button(app, text="RESET", command=reset)
reset_button.grid(row=4, column=0, columnspan=2)

# Result Label
result_label = ttk.Label(app, text="Result: ")
result_label.grid(row=5, column=0, columnspan=2)

app.mainloop()
