""" Смирнов Иван - ИУ7-22Б
Лабораторная работа №2 по Python -- 'Методы уточнения корней'

Необходимо вычислить корни функции на отрезке [a; b] (ош-1) методом Брента
(библиотечная реализация). Отрезок делится на элементарные с шагом h (ош-2). На каждом элементарном
отрезке не более одного корня (ош-3). Для каждого элементарного отрезка с корнем
итерационно вычисляется значение корня с точностью eps. Количество итераций
ограничивается числом Nmax.
Исходные данные: функция в аналитическом виде, [a; b], h, Nmax, eps.

Вывод:
1) - Таблица
----------------------------------------------------------------------
| № корня | [x_i, x_i+1] | x' | f(x') | Кол-во итераций | Код ошибки |
----------------------------------------------------------------------
----------------------------------------------------------------------

2) - График функции (matplotlib)
- Отмечается корни, экстремумы, точки перегиба.

Вариант 17:
"""

# Импортируем модули
from math import *
from Brent import brent

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np

# Функция f
def f(x):
    return eval(entry_f.get())

# График функции
def plot(a, b):
    # Создаем фигуру
    fig = Figure(figsize=(5, 5))
    a_f = fig.add_subplot()

    # Значения, по которым строится график
    X = np.linspace(a, b, int((b-a)*1000))
    Y = np.array([f(i) for i in X])
    Y_diff_1 = np.diff(Y)
    Y_diff_2 = np.diff(Y_diff_1)

    m = np.abs(Y) < 1e-3
    m1 = np.abs(Y_diff_1) < 1e-5
    m2 = np.abs(Y_diff_2) < 1e-8

    # Обозначения
    a_f.plot(X, Y, "--", label="func")
    a_f.scatter(X[m], Y[m], color="green", s=40, marker="o", label="корни")
    a_f.scatter(X[:-1][m1], Y[:-1][m1], color="blue", s=40, marker="o", label="экстремумы")
    a_f.scatter(X[:-2][m2], Y[:-2][m2], color="red", s=40, marker="o", label="точки перегиба")
    a_f.legend(bbox_to_anchor=(0, 1), loc="upper left")
    a_f.grid()
    a_f.set_ylabel(str(entry_f.get()))
    a_f.set_xlabel("x")

    # Отрисовка графика в tkinter
    canvas = FigureCanvasTkAgg(fig, window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=6, column=0, rowspan=3, columnspan=12, stick="wens")

# разбить на отрезки
def intervals(a, b, h):
	x_0 = a
	x_1 = x_0 + h
	arr = []
        
    # Корни на краях
	if f(a) == 0:
		arr.append((a, a + h))
	if f(b) == 0:
		arr.append((b - h, b))

    # Перебираем все интервалы          
	while (x_0 < b):
		if f(x_1) == 0:
			arr.append((x_0, x_1))
		elif f(x_0) * f(x_1) < 0:
			arr.append((x_0, x_1))
		x_0 += h
		x_1 += h
	return arr

# Нажали на кнопку старт
def start():
    try:
        # Получили введенные значения
        a = float(entry_a.get())
        b = float(entry_b.get())
        h = float(entry_h.get())
        nmax = int(entry_nmax.get())
        eps = float(entry_eps.get())

        # Проверяем ошибочные случаи
        if a >= b:
            error(2)
            return
        elif h <= 0:
            error(3)
            return
        elif nmax <= 0:
            error(4)
            return
        elif eps <= 0 or eps > 1:
            error(5)
            return 
        
        # Создаем список интервалов и уточняем корни
        arr = intervals(a, b, h)
        table_arr = []
        for i in range(len(arr)):
            table_arr.append([i+1]+brent(arr[i][0], arr[i][1], eps, nmax, f))

        # Перерисовываем таблицу
        table = ttk.Treeview(window)
        table.grid(row=3, column=0, columnspan=6)
        heads = ["№ корня", "[xi; x(i+1)]", "x'", "f(x')", "N", "Код"]
        table["columns"] = heads
        for header in heads:
            table.heading(header, text=header, anchor='center')
        for row in table_arr:
            table.insert("", tk.END, values=row)
    except Exception:
        error(1)
        return
    plot(a, b)

# Окно с ошибкой
def error(ind):
    err = ["0", "1 - Мало введенных аргументов",
           "2 - Конец интервала должен быть строго больше начала",
           "3 - Шаг должен быть положительным",
           "4 - Количество итераций должно быть больше нуля",
           "5 - Точность должна находиться в диапазоне (0, 1]"]
    messagebox.showerror("Ошибка", err[ind])
    
# Начало - создание окна
window = tk.Tk()
window.geometry("1400x830")
window.resizable(width=False, height=True)
window.title("Lab-2")

# Создание лейблов и полей ввода для:
# 1) Функция
entry_f = tk.Entry(window)
entry_f.grid(row=2, column=0, stick="w")
lb_f = tk.Label(window, text="func:")
lb_f.grid(row=1, column=0, stick="w")
# 2) Начало отрезка
entry_a = tk.Entry(window)
entry_a.grid(row=2, column=1, stick="w")
lb_f = tk.Label(window, text="a:")
lb_f.grid(row=1, column=1, stick="w")
# 3) Конец отрезка
entry_b = tk.Entry(window)
entry_b.grid(row=2, column=2, stick="w")
lb_f = tk.Label(window, text="b:")
lb_f.grid(row=1, column=2, stick="w")
# 4) Шаг разбиения
entry_h = tk.Entry(window)
entry_h.grid(row=2, column=3, stick="w")
lb_f = tk.Label(window, text="h:")
lb_f.grid(row=1, column=3, stick="w")
# 5) Макс. кол-во итераций
entry_nmax = tk.Entry(window)
entry_nmax.grid(row=2, column=4, stick="w")
lb_f = tk.Label(window, text="Nmax:")
lb_f.grid(row=1, column=4, stick="w")
# 6) Точность
entry_eps = tk.Entry(window)
entry_eps.grid(row=2, column=5, stick="w")
lb_f = tk.Label(window, text="eps:")
lb_f.grid(row=1, column=5, stick="w")

# Таблица
table = ttk.Treeview(window)
table.grid(row=3, column=0, columnspan=6, stick="wens")
heads = ["№ корня", "[xi; x(i+1)]", "x'", "f(x')", "N", "Код"]
table["columns"] = heads
for header in heads:
	table.heading(header, text=header)
table_arr = [("", "", "", "", "", "")]
for row in table_arr:
	table.insert("", tk.END, values=row)

# Кнопка старта программы
startButton = tk.Button(text="start", command=start)
startButton.grid(row=0, stick="wens")

window.mainloop()
