# grid layout manager

import tkinter as tk

window = tk.Tk()
window.geometry("600x600")

label1 = tk.Label(window, text="Hello Python 1", bg="white", fg="black")
label1.grid(row=0, column=0, padx=10, pady=10)

label2 = tk.Label(window, text="Hello Python 2", bg="white", fg="black")
label2.grid(row=0, column=1, padx=10, pady=10)

label3 = tk.Label(window, text="Hello Python 3", bg="white", fg="black")
label3.grid(row=0, column=2, padx=10, rowspan=2)

label4 = tk.Label(window, text="Hello Python 4", bg="white", fg="black")
label4.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

label5 = tk.Label(window, text="Hello Python 5", bg="white", fg="black")
label5.grid(row=1, column=2, padx=10, pady=10)

window.mainloop()