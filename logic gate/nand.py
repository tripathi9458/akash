# nand.py
import tkinter as tk

from nand_and_gate import calculate_and_gate

def NAND(a, b):
    if a == 1 and b == 1:
        return False
    else:
        return True

def calculate_nand_gate():
    input_a = var_a.get()
    input_b = var_b.get()
    result = NAND(input_a, input_b)
    result_label.config(text=f"Result: {result}")

# Create the main window
root = tk.Tk()
root.title("NAND and AND Gate Calculator")
root.geometry("300x150")  # Set window size (width x height)

# Create variables for input A and input B
var_a = tk.BooleanVar()
var_b = tk.BooleanVar()

# Create labels and entry widgets for input A and input B
label_a = tk.Label(root, text="Input A:")
entry_a = tk.Checkbutton(root, variable=var_a)

label_b = tk.Label(root, text="Input B:")
entry_b = tk.Checkbutton(root, variable=var_b)

# Create buttons to calculate NAND and AND gate results
calculate_nand_button = tk.Button(root, text="Calculate NAND", command=calculate_nand_gate)
calculate_and_button = tk.Button(root, text="Calculate AND", command=calculate_and_gate)  # Fix the typo here

# Create a label to display the result
result_label = tk.Label(root, text="Result: ")

# Organize widgets using the grid layout
label_a.grid(row=0, column=0)
entry_a.grid(row=0, column=1)
label_b.grid(row=1, column=0)
entry_b.grid(row=1, column=1)
calculate_nand_button.grid(row=2, column=0)
calculate_and_button.grid(row=2, column=1)  # Fix the typo here
result_label.grid(row=3, column=0, columnspan=2)

# Start the main event loop
root.mainloop()
