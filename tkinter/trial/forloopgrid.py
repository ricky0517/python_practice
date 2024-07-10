import tkinter as tk

window = tk.Tk()
window.geometry("500x500")

for i in range(4):
    for j in range(5):
        label = tk.Label(window, text="Python", bg="blue", fg="white")
        label.grid(row=i, column=j, padx=2, pady=2)

window.mainloop()