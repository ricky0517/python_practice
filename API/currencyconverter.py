import tkinter as tk
import tkinter.ttk as ttk
import requests

# http://api.exchangeratesapi.io/latest?base=USD&symbols=USD,INR
base_url = "http://api.exchangeratesapi.io/latest"


def convert_press():
    amount = input_text.get()
    from_curr = source_value.get()
    to_curr = target_value.get()
    main_url = base_url + "?base=" + from_curr + "&symbols=" + from_curr + "," + to_curr
    req = requests.get(main_url)
    result = req.json()
    from_result = result["rates"][from_curr]
    to_result = result["rates"][to_curr]
    converted_amount = round(float(amount) * to_result, 2)
    converted_label.config(text=str(converted_amount)+" "+to_curr)


if __name__ == '__main__':
    main_window = tk.Tk()
    main_window.title("Currency Converter")
    main_window.geometry("400x400")

    intro_label = tk.Label(main_window, text="Welcome to live Currency Converter", bg="blue",
                           fg="white", font="Courier 20 bold", relief=tk.RAISED, borderwidth=3)
    main_window.grid_columnconfigure(0, weight=1)
    intro_label.grid(row=1)

    input_text = tk.StringVar()
    currency_field = tk.Entry(main_window, justify="right", textvariable=input_text)
    currency_field.grid(row=2, padx=5, pady=5)

    country_code = ["INR", "USD", "CAD", "CNY", "DDK", "EUR"]
    source_v = tk.StringVar()
    source_value = ttk.Combobox(main_window, values=country_code, textvariable=source_v)
    source_value.grid(row=3)
    source_value.current(0)

    target_v = tk.StringVar()
    target_value = ttk.Combobox(main_window, values=country_code, textvariable=target_v)
    target_value.grid(row=4)
    target_value.current(1)

    convert_button = tk.Button(main_window, text="Convert", height=1, width=1, command=lambda: convert_press())
    convert_button.grid(row=5)

    converted_label = tk.Label(text="")
    converted_label.grid(row=6)

    main_window.mainloop()
