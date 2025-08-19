# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 20:01:56 2025

@author: mattg
"""

import tkinter as tk
from tkinter import messagebox

# Define the Calculator class
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            return "Error: Division by zero"
        return self.a / self.b

# Function to perform calculation
def perform_operation(op):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        calc = Calculator(num1, num2)
        if op == "add":
            result.set(f"Sum: {calc.add()}")
        elif op == "subtract":
            result.set(f"Difference: {calc.subtract()}")
        elif op == "multiply":
            result.set(f"Product: {calc.multiply()}")
        elif op == "divide":
            res = calc.divide()
            result.set(f"Quotient: {res}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# GUI setup
root = tk.Tk()
root.title("Simple Calculator")

tk.Label(root, text="Enter first number:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter second number:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Button(root, text="Add", command=lambda: perform_operation("add")).grid(row=2, column=0)
tk.Button(root, text="Subtract", command=lambda: perform_operation("subtract")).grid(row=2, column=1)
tk.Button(root, text="Multiply", command=lambda: perform_operation("multiply")).grid(row=3, column=0)
tk.Button(root, text="Divide", command=lambda: perform_operation("divide")).grid(row=3, column=1)

result = tk.StringVar()
tk.Label(root, textvariable=result, fg="blue").grid(row=4, column=0, columnspan=2)

root.mainloop()
