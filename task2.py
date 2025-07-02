import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operator.get()
        if operation == '+':
            result.set(num1 + num2)
        elif operation == '-':
            result.set(num1 - num2)
        elif operation == '*':
            result.set(num1 * num2)
        elif operation == '/':
            if num2 != 0:
                result.set(num1 / num2)
            else:
                messagebox.showerror("Error", "Division by zero")
        else:
            messagebox.showerror("Error", "Invalid operation")
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result.set('')

root = tk.Tk()
root.title("Calculator")

entry1 = tk.Entry(root)
entry1.grid(row=0, column=0)

operator = tk.StringVar()
operator.set('+')
operator_menu = tk.OptionMenu(root, operator, '+', '-', '*', '/')
operator_menu.grid(row=0, column=1)

entry2 = tk.Entry(root)
entry2.grid(row=0, column=2)

button = tk.Button(root, text="Calculate", command=calculate)
button.grid(row=1, column=0, pady=5)

clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.grid(row=1, column=2, pady=5)

result = tk.StringVar()
result_label = tk.Label(root, text="Result:", font=("Arial", 10))
result_label.grid(row=2, column=0)

result_display = tk.Label(root, textvariable=result, font=("Arial", 10, "bold"))
result_display.grid(row=2, column=1, columnspan=2)

root.mainloop()
