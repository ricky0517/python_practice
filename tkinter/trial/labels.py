import tkinter as tk

main_window = tk.Tk()
label1 = tk.Label(main_window, text="Hello, hey there", bg="white", fg="blue",
                  padx=100, pady=200, font="comicsansms 32 bold",
		 borderwidth = 300, relief = "sunken")
# flat grove raised ridge solid sunken

label1.pack()
main_window.mainloop()
