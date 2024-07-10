import tkinter as tk
import tkinter.ttk as ttk


def on_click(a):
    print(combobox1.get())


main_window = tk.Tk()
combobox1 = ttk.Combobox(main_window)
combobox1['values'] = [1, 2, 3, 4, 5, 6]
combobox1.current(0)
combobox1.bind("<<ComboboxSelected>>", on_click)
combobox1.pack()

main_window.mainloop()
