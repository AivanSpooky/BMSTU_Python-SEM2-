""" Смирнов Иван - ИУ7-22Б
Лабораторная работа №1 по Python -- 'Калькулятор систем счисления'

Приложение, используя модуль создания оконных приложений Tkinter, реализует индивидуальное задание
(по варианту). Интерфейс предоставляет ввод символов: как числовых, так и знаков операций
 -- и с использованием клавиатуры, и с помощью кнопок приложения.
Также в приложении создано меню, в котором есть следующие пункты:
 - заданные действия,
 - очистка полей ввода/вывода (по одному и всех сразу),
 - информация о программе и авторе.
Встроенные функции bin(), oct(), hex() не используются.
Программа состоит из нескольких модулей (3), что обеспечивает
разделение реализаций интерфейсной и логической частей. 

Вариант 17: Сложение и вычитание вещественных чисел в 8-й системе счисления
"""

# Импортируем модули
import tkinter as tk
from tkinter.messagebox import showinfo
from funcs import *



# Интерфесная часть
dot_trigger = False # переменная отвечающая за точку

# Результат действий
def equal(entry):
    global dot_trigger
    st = mathoperations(entry.get())
    entry['state'] = tk.NORMAL
    value = entry.get()
    if value == "0":
        return
    entry.delete(0, tk.END)
    entry.insert(0, st)
    value = entry.get()
    if "." not in value:
        dot_trigger = False
    else:
        dot_trigger = True
    entry['state'] = tk.DISABLED

# Очистка поля
def clear(entry):
    global dot_trigger
    entry['state'] = tk.NORMAL
    entry.delete(0, tk.END)
    entry.insert(0, 0)
    dot_trigger = False
    entry['state'] = tk.DISABLED

# Удалить последний символ из поля
def clearS(entry):
    global dot_trigger
    entry['state'] = tk.NORMAL
    value = entry.get()
    entry.delete(0, tk.END)
    if value[-1] == ".":
        dot_trigger = False
    if len(value[:-1]) == 0:
        entry.insert(0, 0)
    else:
        entry.insert(0, value[:-1])
    entry['state'] = tk.DISABLED

# Добавить цифру и точку в поле ввода
def add_digit_or_dot(digit):
    global dot_trigger
    entry['state'] = tk.NORMAL
    value = entry.get()
    if digit == ".":
        if dot_trigger:
            digit = ""
        else:
            dot_trigger = True
    if digit == "+" or digit == "-":
        if value[-1]=="+" or value[-1]=="-" or value[-1]==".":
            digit = ""
        else:
            dot_trigger = False
    if value[0]=='0' and len(value) == 1 and digit != '.':
        if digit != "+":
            value = value[1:]
        else:
            digit = ""
    elif (value[-1]=="+" or value[-1]=="-") and digit == ".":
        digit = "0."
    entry.delete(0, tk.END)
    entry.insert(0, value + digit)
    entry['state'] = tk.DISABLED

# Функции выпадающего меню
def authorInfo():
    showinfo("Об авторе", "Калькулятор 8-ой системы исчесления\nСделал Смирнов Иван (ИУ7-22Б)")
def cl():
    clear(entry)
def clS():
    clearS(entry)
def eq():
    equal(entry)

# Нажатия на клавиатуру
def press_key(event):
    if event.char == "c":
        clearS(entry)
    elif event.char == "C":
        clear(entry)
    elif event.char == "=":
        equal(entry)
    if event.char.isdigit() or event.char == "." or event.char == "+" or event.char == "-":
        add_digit_or_dot(event.char)

# Создание основных кнопок
def makeButton(buttonText):
    if buttonText == "C":
        return tk.Button(text=buttonText, bg='green', fg='white', height= 5, width=10, font=('Times New Roman', 13, ), command=lambda: clear(entry))
    elif buttonText == "=":
        return tk.Button(text=buttonText, bg='green', fg='white', height= 5, width=10, font=('Times New Roman', 13, ), command=lambda: equal(entry))
    elif buttonText == "CE":
        return tk.Button(text=buttonText, bg='green', fg='white', height= 5, width=10, font=('Times New Roman', 13, ), command=lambda: clearS(entry))
    else:
        return tk.Button(text=buttonText, bg='green', fg='white', height= 5, width=10, font=('Times New Roman', 13, ), command=lambda: add_digit_or_dot(buttonText))
    

# Главная часть
# Cоздаем корневой объект - окно
root = tk.Tk()     
root.title("Калькулятор систем счисления")     # устанавливаем заголовок окна
root.geometry("600x550")    # устанавливаем размеры окна
# Блокировка изменения размера окна
root.resizable(width=False, height=False)
root.configure(bg='lime')


root.bind('<Key>', press_key)



# создание надписи ВВОД и поля ввода
entry = tk.Entry(root, justify=tk.RIGHT, font=('Times New Roman', 30), width=15)
entry.grid(row=0, column=1, rowspan=2, columnspan=3, stick='wens', padx=5)
entry.insert(0, 0)
entry['state'] = tk.DISABLED

# Основное меню
mmenu = tk.Menu(root)
root.config(menu=mmenu)

# Создание основных кнопок
makeButton('5').grid(row=3, column=1, padx=5, pady=5)
makeButton('6').grid(row=3, column=2, padx=5, pady=5)
makeButton('7').grid(row=3, column=3, padx=5, pady=5)

makeButton('2').grid(row=4, column=1, padx=5, pady=5)
makeButton('3').grid(row=4, column=2, padx=5, pady=5)
makeButton('4').grid(row=4, column=3, padx=5, pady=5)

makeButton('+').grid(row=5, column=1, padx=5, pady=5)
makeButton('0').grid(row=5, column=2, padx=5, pady=5)
makeButton('1').grid(row=5, column=3, padx=5, pady=5)


makeButton('.').grid(row=6, column=1, padx=5, pady=5)
makeButton('=').grid(row=6, column=2, padx=5, pady=5)
makeButton('-').grid(row=6, column=3, padx=5, pady=5)


makeButton('C').grid(row=4, column=4, padx=5, pady=5)
makeButton('CE').grid(row=3, column=4, padx=5, pady=5)

# Меню Действия
pmenu = tk.Menu(mmenu, tearoff=0)
pmenu.add_command(label="Посчитать", command=eq)
pmenu.add_command(label="Удалить поле", command=cl)
pmenu.add_command(label="Удалить символ", command=clS)
mmenu.add_cascade(label="Действия", menu=pmenu)

# Меню Информация
amenu = tk.Menu(mmenu, tearoff=0)
amenu.add_command(label="Об авторе", command=authorInfo)
mmenu.add_cascade(label="Информация", menu=amenu)



clear(entry)

root.mainloop()
