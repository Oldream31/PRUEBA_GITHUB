import tkinter as tk

def calculate():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(result))

root = tk.Tk()
root.title("Calculadora")

entry = tk.Entry(root, width=16, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row = 1
col = 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, width=4, height=2, font=('Arial', 12), command=lambda text=button_text: entry.insert(tk.END, text))
    button.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()