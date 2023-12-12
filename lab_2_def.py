# Смирнов Иван ИУ7-22Б Защита - Граф интерфейс
# Нет шага (отр с одним корнем)
# Метод хорд

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from math import *

def f(x):
    return eval(entry_f.get())

def hords(a, b, eps):
    const_a = a
    const_b = b
    c1 = a
    for i in range(100):
        y_a = f(a)
        y_b = f(b)
        if abs((y_a-y_b))<1e-50:
            c2 = a - (y_a * (a-b))/1e-50
        else:
            c2 = a - (y_a * (a-b))/(y_a-y_b)
        y_c = f(c2)
        if abs(c1-c2)<eps:
            if const_a <= c2 <= const_b:
                return [f"[{const_a:.6g};{const_b:.6g}]", f"{c2:.6g}", f"{f(c2):.6g}", 0]
            else:
                return [f"[{const_a:.6g};{const_b:.6g}]", f"корня нет", f"корня нет", 1]
        if (y_a < 0 and y_c > 0) or (y_a > 0 and y_c < 0):
            b = c2
        else:
            a = c2
            c1 = c2
    if const_a <= c1 <= const_b:
        return [f"[{const_a:.6g};{const_b:.6g}]", f"{c1:.6g}", f"{f(c1):.6g}", 0]
    else:
        return [f"[{const_a:.6g};{const_b:.6g}]", f"корня нет", f"корня нет", 1]

def start():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        eps = float(entry_eps.get())
        if a >= b:
            error(1)
            return
        elif eps <= 0 or eps > 1:
            error(2)
            return
    except Exception:
        error(0)
        return
    
    table_arr = []
    table_arr.append(hords(a, b, eps))   
    table = ttk.Treeview(window)
    table.grid(row=3, column=0, columnspan=6, stick="wens")
    heads = ["[xi; x(i+1)]", "x'", "f(x')", "Код"]
    table["columns"] = heads
    for header in heads:
        table.heading(header, text=header)
    for row in table_arr:
        table.insert("", tk.END, values=row)

def error(i):
    er = ["Данные введены некорректно!", "Начало отрезка должно\
быть строго меньше конца", "Должно выполняться равенство 0 < eps <= 1!"]
    messagebox.showerror("Ошибка", er[i])
    
    
window = tk.Tk()
window.geometry("1000x400")
window.resizable(width=False, height=False)
window.title("Lab-2 def")

entry_f = tk.Entry(window)
entry_f.grid(row=2, column=0)
l_f = tk.Label(window, text="f")
l_f.grid(row=1, column=0)

entry_a = tk.Entry(window)
entry_a.grid(row=2, column=1)
l_a = tk.Label(window, text="a")
l_a.grid(row=1, column=1)

entry_b = tk.Entry(window)
entry_b.grid(row=2, column=2)
l_b = tk.Label(window, text="b")
l_b.grid(row=1, column=2)

entry_eps = tk.Entry(window)
entry_eps.grid(row=2, column=3)
l_b = tk.Label(window, text="eps")
l_b.grid(row=1, column=3)

startButton = tk.Button(text="start", command=start)
startButton.grid(row=0, stick="wens")

table = ttk.Treeview(window)
table.grid(row=3, column=0, columnspan=6, stick="wens")
heads = ["[xi; x(i+1)]", "x'", "f(x')", "Код"]
table["columns"] = heads
for header in heads:
	table.heading(header, text=header)
table_arr = [("", "", "", "")]
for row in table_arr:
	table.insert("", tk.END, values=row)

window.mainloop()
