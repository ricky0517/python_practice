import tkinter as tk

main_window = tk.Tk()
main_window.title("Calculator")
main_window.geometry("400x300")

expression = ""


def key_press(key):
    global expression
    expression = expression + str(key)
    input_text.set(expression)


def key_clear():
    global expression
    expression = ""
    input_text.set(expression)


def key_equal():
    result = eval(expression)
    input_text.set(result)


input_text = tk.StringVar()
expression_field = tk.Entry(main_window, font="Ariel 16 bold", justify="right", textvariable=input_text)
expression_field.grid(row=1, column=1, columnspan=4, ipadx=70)

button1 = tk.Button(main_window, text="1", height=2, width=7, command=lambda: key_press("1"))
button1.grid(row=2, column=1, sticky="nsew")
button2 = tk.Button(main_window, text="2", height=2, width=7, command=lambda: key_press("2"))
button2.grid(row=2, column=2, sticky="nsew")
button3 = tk.Button(main_window, text="3", height=2, width=7, command=lambda: key_press("3"))
button3.grid(row=2, column=3, sticky="nsew")
button4 = tk.Button(main_window, text="4", height=2, width=7, command=lambda: key_press("4"))
button4.grid(row=3, column=1, sticky="nsew")
button5 = tk.Button(main_window, text="5", height=2, width=7, command=lambda: key_press("5"))
button5.grid(row=3, column=2, sticky="nsew")
button6 = tk.Button(main_window, text="6", height=2, width=7, command=lambda: key_press("6"))
button6.grid(row=3, column=3, sticky="nsew")
button7 = tk.Button(main_window, text="7", height=2, width=7, command=lambda: key_press("7"))
button7.grid(row=4, column=1, sticky="nsew")
button8 = tk.Button(main_window, text="8", height=2, width=7, command=lambda: key_press("8"))
button8.grid(row=4, column=2, sticky="nsew")
button9 = tk.Button(main_window, text="9", height=2, width=7, command=lambda: key_press("9"))
button9.grid(row=4, column=3, sticky="nsew")
button0 = tk.Button(main_window, text="0", height=2, width=7, command=lambda: key_press("0"))
button0.grid(row=5, column=1, sticky="nsew")

button_clear = tk.Button(main_window, text="clear", height=2, width=7, command=lambda: key_clear())
button_clear.grid(row=5, column=2, sticky="nsew")
button_equal = tk.Button(main_window, text="=", height=2, width=7, command=lambda: key_equal())
button_equal.grid(row=5, column=3, sticky="nsew")
button_plus = tk.Button(main_window, text="+", height=2, width=7, command=lambda: key_press("+"))
button_plus.grid(row=2, column=4, sticky="nsew")
button_minus = tk.Button(main_window, text="-", height=2, width=7, command=lambda: key_press("-"))
button_minus.grid(row=3, column=4, sticky="nsew")
button_divide = tk.Button(main_window, text="/", height=2, width=7, command=lambda: key_press("/"))
button_divide.grid(row=5, column=4, sticky="nsew")
button_multiply = tk.Button(main_window, text="*", height=2, width=7, command=lambda: key_press("*"))
button_multiply.grid(row=4, column=4, sticky="nsew")

main_window.mainloop()
