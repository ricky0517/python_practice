import tkinter as ct

window = ct.Tk()
window.title("Go Pro")
label = ct.Label(window, text="Welcome to terminal coding",bg="white",fg="red")
label.pack()

# adding photo to UI
photo = ct.PhotoImage(file="img.png")
label2 = ct.Label(image=photo)
label2.pack()

window.mainloop()