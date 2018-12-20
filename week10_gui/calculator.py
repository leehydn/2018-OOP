import tkinter as tk

expression = ""


def press(value):
    global expression

    expression = expression + str(value)
    equation.set(expression)


def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("error")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Calculator")
    window.configure(background='white')
    
    expression_frame = tk.Frame(window, borderwidth=20, relief=tk.SUNKEN)
    equation = tk.StringVar()
    expression_field = tk.Entry(expression_frame, textvariable=equation, width=30)

    expression_field.grid(columnspan=4)
    expression_frame.grid(columnspan=4)
    equation.set('enter your expression')

    button1 = tk.Button(window, text=' 1 ', fg='#000000', bg='#F0F0F0',
                     command=lambda: press(1), relief=tk.RAISED, height=3, width=5, borderwidth=6)
    button1.grid(row=2, column=0)
    button2 = tk.Button(window, text=' 2 ', fg='#000000', bg='#F0F0F0',
                     command=lambda: press(2), relief=tk.RAISED, height=3, width=5, borderwidth=6)
    button2.grid(row=2, column=1)
    button3 = tk.Button(window, text=' 3 ', fg='#000000', bg='#F0F0F0',
                     command=lambda: press(3), relief=tk.RAISED, height=3, width=5, borderwidth=6)
    button3.grid(row=2, column=2)
    button4 = tk.Button(window, text=' 4 ', fg='#000000', bg='#F0F0F0',
                     command=lambda: press(4), relief=tk.RAISED, height=3, width=5, borderwidth=6)
    button4.grid(row=3, column=0)
    button5 = tk.Button(window, text=' 5 ', fg='#000000', bg='#F0F0F0',
                     command=lambda: press(5), relief=tk.RAISED, height=3, width=5, borderwidth=6)
    button5.grid(row=3, column=1)
    button6 = tk.Button(window, text=' 6 ', fg='#000000', bg='#F0F0F0',
                     command=lambda: press(6), relief=tk.RAISED, height=3, width=5, borderwidth=6)
    button6.grid(row=3, column=2)
    button7 = tk.Button(window, text=' 7 ', fg='#000000', bg='#F0F0F0',
                     command=lambda: press(7), relief=tk.RAISED, height=3, width=5, borderwidth=6)
    button7.grid(row=4, column=0)
    button8 = tk.Button(window, text=' 8 ', fg='#000000', bg='#F0F0F0',
                     command=lambda: press(8), relief=tk.RAISED, height=3, width=5, borderwidth=6)
    button8.grid(row=4, column=1)
    button9 = tk.Button(window, text=' 9 ', fg='#000000', bg='#F0F0F0',
                     command=lambda: press(9), relief=tk.RAISED, height=3, width=5, borderwidth=6)
    button9.grid(row=4, column=2)
    button0 = tk.Button(window, text=' 0 ', fg='#000000', bg='#F0F0F0',
                     command=lambda: press(0), relief=tk.RAISED, height=3, width=5, borderwidth=6)
    button0.grid(row=5, column=1)
    plus = tk.Button(window, text=' + ', fg='#000000', bg='#F0F0F0',
                  command=lambda: press("+"), relief=tk.RAISED, height=3, width=5, borderwidth=6)
    plus.grid(row=2, column=3)
    minus = tk.Button(window, text=' - ', fg='#000000', bg='#F0F0F0',
                   command=lambda: press("-"), relief=tk.RAISED, height=3, width=5, borderwidth=6)
    minus.grid(row=3, column=3)
    multiply = tk.Button(window, text=' * ', fg='#000000', bg='#F0F0F0',
                      command=lambda: press("*"), relief=tk.RAISED, height=3, width=5, borderwidth=6)
    multiply.grid(row=4, column=3)
    divide = tk.Button(window, text=' / ', fg='#000000', bg='#F0F0F0',
                    command=lambda: press("/"), relief=tk.RAISED, height=3, width=5, borderwidth=6)
    divide.grid(row=5, column=3)
    equal = tk.Button(window, text=' = ', fg='#000000', bg='#F0F0F0',
                   command=equalpress, relief=tk.RAISED, height=3, width=5, borderwidth=6)
    equal.grid(row=5, column=2)
    clear = tk.Button(window, text='C', fg='#000000', bg='#F0F0F0',
                   command=clear, relief=tk.RAISED, height=3, width=5, borderwidth=6)
    clear.grid(row=5, column=0)

    # start the GUI
    window.mainloop()
