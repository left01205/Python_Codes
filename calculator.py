import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    result = eval(expression)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '1', '2', '3', '+',
    '4', '5', '6', '-',
    '7', '8', '9', '*',
    '0', 'C', '=', '/'
]

row_val = 1
col_val = 0

for button_text in buttons:
    if button_text == '=':
        button = tk.Button(root, text=button_text, padx=20, pady=10, command=button_equal)
    elif button_text == 'C':
        button = tk.Button(root, text=button_text, padx=20, pady=10, command=button_clear)
    else:
        button = tk.Button(root, text=button_text, padx=20, pady=10, command=lambda text=button_text: button_click(text))
    button.grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()