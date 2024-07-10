import tkinter as tk

main_window = tk.Tk()
main_window.title("Interface : UI")
# to create boundaries
main_window.geometry("800x600")

# to set boundary like min max
main_window.minsize(400, 300)
main_window.maxsize(1000, 800)

main_window.mainloop()  # important

# widgets frame, label, button, checkbutton, radiobutton, entry, combobox(dropdown)
