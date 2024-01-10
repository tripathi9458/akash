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

def XNOR(a, b):
    if a == b:
        return 1
    else:
        return 0

def calculate_xnor_gate():
    input_a = var_a.get()
    input_b = var_b.get()
    result = XNOR(input_a, input_b)
    result_label.config(text=f"XNOR Result: {result}")

def calculate_not_gate():
    input_a = var_a.get()
    result = NOT(input_a)
    result_label.config(text=f"NOT Result: {result}")

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

# Create the main window
root = tk.Tk()
root.title("Gate Calculator")
root.geometry("700x630+400+10")  # Set window size (width x height)
root.configure(bg='#7FB8D8')  # Set background color

# Create variables for input A and input B
var_a = tk.BooleanVar()
var_b = tk.BooleanVar()

# Create labels and entry widgets for input A and input B
label_a = tk.Label(root, text="Input A:",font=("time new roman",27,"bold"), bg='#7FB8D8', width=20)
entry_a = tk.Checkbutton(root, variable=var_a, bg='#7FB8D8', width=20,activebackground="#7FB8D8")

label_b = tk.Label(root, text="Input B:",font=("time new roman",27,"bold"), bg='#7FB8D8', width=20)
entry_b = tk.Checkbutton(root, variable=var_b, bg='#7FB8D8', width=20, fg='black',activebackground="#7FB8D8")

# Create buttons to calculate XNOR, NOT, XOR, OR, NOR, and AND gate results
calculate_xnor_button = tk.Button(root, text="Calculate XNOR",font=("time new roman",27,"bold"), command=calculate_xnor_gate, bg='#8A2BE2', fg='white',activebackground="#8A2BE2", width=30)
calculate_not_button = tk.Button(root, text="Calculate NOT", font=("time new roman",27,"bold"),command=calculate_not_gate, bg='#800000', fg='white',activebackground="#800000", width=30)
calculate_xor_button = tk.Button(root, text="Calculate XOR",font=("time new roman",27,"bold"), command=calculate_xor_gate, bg='#2E8B57', fg='white',activebackground="#2E8B57", width=30)
calculate_or_button = tk.Button(root, text="Calculate OR", font=("time new roman",27,"bold"),command=calculate_or_gate, bg='#4169E1', fg='white',activebackground="#4169E1", width=30)
calculate_nor_button = tk.Button(root, text="Calculate NOR",font=("time new roman",27,"bold"), command=calculate_nor_gate, bg='#FF6347', fg='white',activebackground="#FF6347", width=30)
calculate_and_button = tk.Button(root, text="Calculate AND",font=("time new roman",27,"bold"), command=calculate_and_gate, bg='#FFD700', fg='black',activebackground="#FFD700", width=30)

# Create a label to display the result
result_label = tk.Label(root, text="Result: ",font=("time new roman",28,"bold"),fg="red", bg='#7FB8D8', width=30)

# Organize widgets using the grid layout
label_a.grid(row=0, column=0)
entry_a.grid(row=0, column=1)
label_b.grid(row=1, column=0)
entry_b.grid(row=1, column=1)
calculate_xnor_button.grid(row=2, column=0, columnspan=2,)
calculate_not_button.grid(row=3, column=0, columnspan=2)
calculate_xor_button.grid(row=4, column=0, columnspan=2)
calculate_or_button.grid(row=5, column=0, columnspan=2)
calculate_nor_button.grid(row=6, column=0, columnspan=2)
calculate_and_button.grid(row=7, column=0, columnspan=2)
result_label.grid(row=8, column=0, columnspan=2)

# Start the main event loop
root.mainloop()
