import tkinter as tk

def get_value():
    print("username:",username_entry.get())
    print("paassword:",password_entry.get())

main_window = tk.Tk()
main_window.geometry("600x600")
main_window.title("Login Page")

username_label = tk.Label(main_window, text="Username:")
password_label = tk.Label(main_window, text="Password:")
username_label.grid(row=0, column=0)
password_label.grid(row=1, column=0)

username_entry = tk.Entry(main_window)
password_entry = tk.Entry(main_window)
username_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)

submit_button = tk.Button(main_window, text="submit", command=get_value)
submit_button.grid(row=3, column=0)

main_window.mainloop()
