import tkinter as tk
import math

def clear_onclick():
        input_screen.configure(text="")
        output_screen.configure(text="")

def operator_onclick(operator):
       new_text = input_screen.cget("text")
       input_screen.configure(text=new_text + operator)

def digit_onclick(digit):
       new_text = input_screen.cget("text")
       input_screen.configure(text=new_text + str(digit))
    

def square_onclick():
    try:
        value = float(input_screen.cget("text"))
        result = value **2
        output_screen.configure(text=str(result))
    except ValueError:
            output_screen.configure(text="Error")

def square_root_onclick():
        try:
                value = float(input_screen.cget("text"))
                if value <0:
                      output_screen.configure(text="Error: Negative Value")
                else:
                       result=math.sqrt(value)
                       output_screen.configure(text=str(result))
        except ValueError:
               output_screen.configure(text="Error")


def evaluate_expression():
    try:
        expression = input_screen.cget("text")
        # Replace symbols with Python-compatible operators
        expression = expression.replace('x', '*').replace('÷', '/')
        result = f'Result: {eval(expression)}'
        output_screen.configure(text=str(result))
    except ZeroDivisionError:
        output_screen.configure(text="Error: Division by Zero")
    except Exception as e:
        output_screen.configure(text="Error")



main = tk.Tk()
main.geometry("300x400")
main.resizable(0,0)
main.title("Calculator")
main.configure(bg="grey")
main.iconbitmap(r'C:\Users\aleja\OneDrive\Escritorio\Vault\Repositories\Calculator\Calculator_Icon.ico')

input_screen = tk.Label(
    main,
    text= "",
    width=22,
    height=2,

    bg="lightBlue",
    highlightbackground="black",
    highlightcolor="blue",
    highlightthickness=1
)
input_screen.place(x=130, y=0)

output_screen = tk.Label(
    main,
    text="",
    width=40,
    height=4,

    bg="lightBlue",
    highlightbackground="black",
    highlightcolor="black",
    highlightthickness=2  
)
output_screen.place(x=5,y=45)

clear_button = tk.Button(
    main,
    text="Clear",
    width=7,
    height=int(2.5),
    command=clear_onclick
)
clear_button.place(x=240, y=132)

equal_button = tk.Button(
    main,
    text="=",
    width=13,
    height=3,
    command=evaluate_expression
    
)
equal_button.place(x=198,y=342)

decimal_button = tk.Button(
    main,
    text=".",
    width= int(7.7),
    height=3,
    command=lambda:digit_onclick('.')
)
decimal_button.place(x=138 , y=342)


negative_button = tk.Button(
    main,
    text = "(-)",
    width=7,
    height= int(2.5),

    command=lambda: digit_onclick("-")
)
negative_button.place(x=180, y=300)


square_button = tk.Button(
    main,
    text="x²",
    width=7,
    height=int(2.5),
    command=square_onclick

)
square_button.place(x=180, y=258)

square_root_button = tk.Button(
    main,
    text="√(",
    width=7,
    height=int(2.5),
    command=square_root_onclick
)
square_root_button.place(x=180, y=216)

zero_button = tk.Button(
    main,
    text="0",
    width=int(18.5),
    height=3,
    command=lambda: digit_onclick(0)
)
zero_button.place(x=0, y=342)

plus_button = tk.Button(
    main,
    text="+",
    width=7,
    height=2,
    command=lambda: operator_onclick("+")
)
plus_button.place(x=240, y=300)

minus_button = tk.Button(
    main,
    text="-",
    width=7,
    height=2,
    command=lambda: operator_onclick("-")
)
minus_button.place(x=240,y=258)

multiplication_button = tk.Button(
    main,
    text= "x",
    width = 7,
    height=2,
    command=lambda: operator_onclick("x")
)
multiplication_button.place(x=240, y=216)

division_button = tk.Button(
    main,
    text = "÷",
    width=7,
    height=2,
    command=lambda: operator_onclick("÷")
)
division_button.place(x=240, y=174)

one_button = tk.Button(
    main,
    text="1",
    width=7,
    height=3,
    command=lambda: digit_onclick(1)
)
one_button.place(x=0, y=285)

two_button = tk.Button(
    main,
    text="2",
    width= 7,
    height=3,
    comman=lambda: digit_onclick(2)
)
two_button.place(x=60, y=285)

three_button = tk.Button(
    main,
    text="3",
    width=7,
    height=3,
    command=lambda: digit_onclick(3)
)
three_button.place(x=120, y=285)

four_button = tk.Button(
    main,
    text="4",
    width=7,
    height=3,
    command=lambda: digit_onclick(4)

)
four_button.place(x=0, y=228)

five_button = tk.Button(
    main,
    text="5",
    width=7,
    height=3,
    command=lambda: digit_onclick(5)
)
five_button.place(x=60,y=228)

six_button = tk.Button(
    main,
    text="6",
    width=7,
    height=3,
    command=lambda: digit_onclick(6)
)
six_button.place(x=120, y=228)

seven_button = tk.Button(
    main,
    text="7",
    width=7,
    height=3,
    command=lambda: digit_onclick(7)
)
seven_button.place(x=0, y=171)

eight_button = tk.Button(
    main,
    text="8",
    width= 7,
    height=3,
    command=lambda: digit_onclick(8)
)
eight_button.place(x=60, y=171)

nine_button = tk.Button(
    main,
    text="9",
    width=7,
    height=3,
    command=lambda: digit_onclick(9)
)
nine_button.place(x=120, y=171)


run = main.mainloop()
