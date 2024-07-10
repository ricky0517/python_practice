import tkinter as tk

mainwindow = tk.Tk()
mainwindow.geometry("500x500")

label1 = tk.Label(mainwindow, text="label1", bg="green", fg="white")
label1.pack(side=tk.BOTTOM)

label12 = tk.Label(mainwindow, text="label12", bg="black", fg="red")
label12.pack(fill=tk.X)

label123 = tk.Label(mainwindow, text="label123", bg="white", fg="red")
label123.pack(side=tk.RIGHT, fill=tk.Y)

# padx pady
label4 = tk.Label(mainwindow, text="label4", bg="white", fg="red")
label4.pack(side=tk.LEFT, padx=10)

label5 = tk.Label(mainwindow, text="label5", bg="white", fg="red")
label5.pack(side=tk.LEFT, padx=40)

label6 = tk.Label(mainwindow, text="label6", bg="white", fg="red")
label6.pack( padx=10, ipadx="20", ipady="40")

label7 = tk.Label(mainwindow, text="label7", bg="white", fg="red")
label7.pack( padx=40)

mainwindow.mainloop()
