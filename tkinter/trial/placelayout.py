import tkinter as tk

window = tk.Tk()
window.geometry("500x500")

label = tk.Label(window, text="Python", bg="gray")
label.place(x=250, y=30)
label.mainloop()