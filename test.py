import tkinter as tk
from tk import ttk


app = tk.Tk()
app.geometry("200x100")

labelTop = tk.Label(app, text="Choose your favourite month")
labelTop.grid(column=0, row=0)

comboExample = ttk.Combobox(app, values=["January", "February", "March", "April"])
comboExample.grid(column=0, row=1)
comboExample.current(1)

comboExample.bind("<<ComboboxSelected>>", callbackFunc)

selected_element = comboExample.get()
print(f"New Element Selected: {selected_element}")

selected_element = comboExample.get()
print(f"New Element Selected: {selected_element}")
app.mainloop()