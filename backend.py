import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create the display
display = tk.Entry(root, width=25, font=('Arial', 16))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, str(current) + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_add():
    first_number = display.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    display.delete(0, tk.END)

def button_subtract():
    first_number = display.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    display.delete(0, tk.END)

def button_multiply():
    first_number = display.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    display.delete(0, tk.END)

def button_divide():
    first_number = display.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    display.delete(0, tk.END)

def button_equal():
    second_number = display.get()
    display.delete(0, tk.END)
    if math == "addition":
        display.insert(0, f_num + int(second_number))
    elif math == "subtraction":
        display.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        display.insert(0, f_num * int(second_number))
    elif math == "division":
        display.insert(0, f_num / int(second_number))

button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = tk.Button(root, text="+", padx=39, pady=20, command=button_add)
button_subtract = tk.Button(root, text="-", padx=41, pady=20, command=button_subtract)
button_multiply = tk.Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = tk.Button(root, text="/", padx=41, pady=20, command=button_divide)
button_equal = tk.Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = tk.Button(root, text="Clear", padx=79, pady=20, command=button_clear)

# Put the buttons on the screen
button_1.pack(side=tk.LEFT)
button_2.pack(side=tk.LEFT)
button_3.pack(side=tk.LEFT)
button_4.pack(side=tk.LEFT)
button_5.pack(side=tk.LEFT)
button_6.pack(side=tk.LEFT)
button_7.pack(side=tk.LEFT)
button_8.pack(side=tk.LEFT)
button_9.pack(side=tk.LEFT)
button_0.pack(side=tk.LEFT)
button_add.pack(side=tk.LEFT)
button_subtract.pack(side=tk.LEFT)
button_multiply.pack(side=tk.LEFT)
button_divide.pack(side=tk.LEFT)
button_equal.pack(side=tk.LEFT)
button_clear.pack(side=tk.LEFT)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_equal.grid(row=4, column=1, columnspan=2)
button_clear.grid(row=4, column=0, columnspan=1)

