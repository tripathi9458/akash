import tkinter as tk

def XOR(a, b):
    if a != b:
        return 1
    else:
        return 0

def OR(a, b):
    if a == 1 or b == 1:
        return True
    else:
        return False

def NOR(a, b):
    if(a == 0) and (b == 0):
        return 1
    elif(a == 0) and (b == 1):
        return 0
    elif(a == 1) and (b == 0):
        return 0
    elif(a == 1) and (b == 1):
        return 0

def AND(a, b):
    if a == 1 and b == 1:
        return True
    else:
        return False

def NOT(a):
    return not a

def calculate_xor_gate():
    input_a = var_a.get()
    input_b = var_b.get()
    result = XOR(input_a, input_b)
    result_label.config(text=f"XOR Result: {result}")

def calculate_or_gate():
    input_a = var_a.get()
    input_b = var_b.get()
    result = OR(input_a, input_b)
    result_label.config(text=f"OR Result: {result}")

def calculate_nor_gate():
    input_a = var_a.get()
    input_b = var_b.get()
    result = NOR(input_a, input_b)
    result_label.config(text=f"NOR Result: {result}")

def calculate_and_gate():
    input_a = var_a.get()
    input_b = var_b.get()
    result = AND(input_a, input_b)
    result_label.config(text=f"AND Result: {result}")

def calculate_not_gate():
    input_a = var_a.get()
    result = NOT(input_a)
    result_label.config(text=f"NOT Result: {result}")

# Create the main window
root = tk.Tk()
root.title("NOT, XOR, OR, NOR, AND Gate Calculator")
root.geometry("300x350")  # Set window size (width x height)

# Create variables for input A and input B
var_a = tk.BooleanVar()
var_b = tk.BooleanVar()

# Create labels and entry widgets for input A and input B
label_a = tk.Label(root, text="Input A:")
entry_a = tk.Checkbutton(root, variable=var_a)

label_b = tk.Label(root, text="Input B:")
entry_b = tk.Checkbutton(root, variable=var_b)

# Create buttons to calculate NOT, XOR, OR, NOR, and AND gate results
calculate_not_button = tk.Button(root, text="Calculate NOT", command=calculate_not_gate)
calculate_xor_button = tk.Button(root, text="Calculate XOR", command=calculate_xor_gate)
calculate_or_button = tk.Button(root, text="Calculate OR", command=calculate_or_gate)
calculate_nor_button = tk.Button(root, text="Calculate NOR", command=calculate_nor_gate)
calculate_and_button = tk.Button(root, text="Calculate AND", command=calculate_and_gate)

# Create a label to display the result
result_label = tk.Label(root, text="Result: ")

# Organize widgets using the grid layout
label_a.grid(row=0, column=0)
entry_a.grid(row=0, column=1)
label_b.grid(row=1, column=0)
entry_b.grid(row=1, column=1)
calculate_not_button.grid(row=2, column=0, columnspan=2)
calculate_xor_button.grid(row=3, column=0, columnspan=2)
calculate_or_button.grid(row=4, column=0, columnspan=2)
calculate_nor_button.grid(row=5, column=0, columnspan=2)
calculate_and_button.grid(row=6, column=0, columnspan=2)
result_label.grid(row=7, column=0, columnspan=2)

# Start the main event loop
root.mainloop()
