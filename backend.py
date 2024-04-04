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
