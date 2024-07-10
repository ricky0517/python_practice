import tkinter as tk

window = tk.Tk()
window.geometry("500x500")
entry = tk.Entry(window, bg="gray", fg="white", justify="right", font="Ariel 20 bold", bd=6)
entry.pack()
window.mainloop()