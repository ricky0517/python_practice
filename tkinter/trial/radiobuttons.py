import tkinter as tk


def click():
    print("radio button clicked:", var.get())


window = tk.Tk()
window.geometry("500x500")
window.title("Radio button Demo")
var = tk.IntVar()
button1 = tk.Radiobutton(window, text="option1", command=click, variable=var, value=1, height=4)
button1.pack()
button2 = tk.Radiobutton(window, text="option2", command=click, width=30, variable=var, value=2)
button2.pack()
button3 = tk.Radiobutton(window, text="option3", command=click, variable=var, value=3)
button3.pack()

window.mainloop()
