import tkinter as tk

root = tk.Tk()
root.title("My Calculator")

e = tk.Entry(root, width=65)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=30)

current = ""
first_number = ""
second_number= ""
f_num = 0
add = 0
sub = 0
mult = 0
div =0


def button_click(number):
    global current
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(current) + str(number))


def button_clear():
    global current, first_number
    current = ""
    first_number = ""
    e.delete(0, tk.END)


def button_add():
    global first_number
    first_number = e.get()
    if first_number != "":
        e.delete(0, tk.END)
        global f_num, add
        f_num = float(first_number)
        add = 1
    else:
        e.insert(0, "")

def button_sub():
    global first_number
    first_number = e.get()
    if first_number !="":
        e.delete(0, tk.END)
        global f_num, sub
        f_num = float(first_number)
        sub = 1
    else:
        e.insert(0, "-")


def button_mult():
    global first_number
    first_number = e.get()
    if first_number != "":
        e.delete(0, tk.END)
        global f_num, mult
        f_num = float(first_number)
        mult = 1
    else:
        e.insert(0, "")

def button_div():
    global first_number
    first_number = e.get()
    if first_number != "":
        e.delete(0, tk.END)
        global f_num, div
        f_num = float(first_number)
        div = 1
    else:
        e.insert(0, "")

def button_equals():
    global f_num, add, sub, mult, div, second_number
    if add == 1:
        second_number = e.get()
        e.delete(0, tk.END)
        s_num = float(second_number)
        global f_num
        e.insert(0, f_num + s_num)
        f_num = 0
        s_num = 0
        add = 0

    if sub==1:
        second_number = e.get()
        e.delete(0, tk.END)
        s_num = float(second_number)
        e.insert(0, f_num - s_num)
        f_num = 0
        s_num = 0
        sub = 0

    if mult==1:
        second_number = e.get()
        e.delete(0, tk.END)
        s_num = float(second_number)
        e.insert(0, f_num * s_num)
        f_num = 0
        s_num = 0
        mult = 0

    if div==1:
        second_number = e.get()
        e.delete(0, tk.END)
        s_num = float(second_number)
        if s_num == 0:
            e.insert(0, "Can't divide by Zero")
        else:
            e.insert(0, f_num / s_num)
        f_num = 0
        s_num = 0
        div = 0


def button_back():
    global first_number, second_number
    if second_number != "":
        e.delete(0, tk.END)
        second_number = ""
    else:
        e.delete(0, tk.END)
        first_number = ""

btn1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1)).grid(row=1, column=0)
btn2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2)).grid(row=1, column=1)
btn3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3)).grid(row=1, column=2)
btn4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4)).grid(row=2, column=0)
btn5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5)).grid(row=2, column=1)
btn6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6)).grid(row=2, column=2)
btn7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7)).grid(row=3, column=0)
btn8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8)).grid(row=3, column=1)
btn9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9)).grid(row=3, column=2)
btn0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0)).grid(row=4, column=1)
btndot = tk.Button(root, text=".", padx=40, pady=20, command=lambda: button_click(".")).grid(row=4, column=0)
btnequals = tk.Button(root, text="=", padx=40, pady=20, command=lambda: button_equals()).grid(row=4, column=2)
btnadd = tk.Button(root, text="+", padx=40, pady=20, command=button_add).grid(row=1, column=3)
btnsub = tk.Button(root, text="-", padx=40, pady=20, command=lambda: button_sub()).grid(row=2, column=3)
btnmult = tk.Button(root, text="*", padx=40, pady=20, command=lambda: button_mult()).grid(row=3, column=3)
btndiv = tk.Button(root, text="/", padx=40, pady=20, command=lambda: button_div()).grid(row=4, column=3)
btnback = tk.Button(root, text="Back", padx=80, pady=20, command=button_back).grid(row=5, column=0, columnspan=2)
btnclear = tk.Button(root, text="Clear", padx=80, pady=20, command=button_clear).grid(row=5, column=2, columnspan=2)
root.mainloop()
