""" Смирнов Иван - ИУ7-22Б
Лабораторная работа №3 по Python -- 'Кодирование в изображениях'
"""

# Импортируем модули
from PIL import Image, ImageDraw
from os.path import exists
import tkinter as tk
from tkinter import messagebox as box
from tkinter import filedialog as fd
from imageOperations import *


# Расшифровка
def decode():
    try:
        filetypes = (('image files', '*.PNG'),)
	
        filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
        name = filename.split("/")[-1]
        image = Image.open(filename)
        draw = ImageDraw.Draw(image)
        width = image.size[0]
        height = image.size[1]
        pix = image.load()

        string = decode_image(width, height, pix)
        box.showinfo("Lab_03", "Сообщение расшифровано!")
        entry_out.delete(0, tk.END)
        entry_out.insert(0, string)
    except Exception:
        error(3)
        return

# Зашифровка
def encode():
    try:
        # Получили введенные значения
        mes = entry_in.get()
        path = entry_p.get()
	    # Проверка на правильность
        if len(mes) == 0 or len(path) == 0:
            raise Exception
        # Тип файлов - .bmp
        filetypes = (('image files', '*.bmp'),)
        # Открыть картинку для шифровки
        filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
        try:
            image = Image.open(filename)
        except Exception:
            return
        draw = ImageDraw.Draw(image)
        width = image.size[0]
        height = image.size[1]
        pix = image.load()
        # Зашифровать сообщение
        end_point = "@"
        mes = mes + end_point
        bin_mes = text_to_binary(mes)
        pix = change_last_bit(width, height, pix, bin_mes, draw)
        # Выбрать путь для сохранения картинки
        folder = fd.askdirectory()
        name = "/" + path
        if name[-4:] != ".png":
            name += ".png"
        image.save(folder + name, "PNG")

        box.showinfo("Lab_03", "Сообщение было зашифровано в картинке!")
    except Exception:
        error(1)
        return

# Окно с ошибкой
def error(ind):
    err = ["0", "1 - Мало введенных аргументов",
           "2 - Файла не существует!",
           "3 - Непредвиденная ошибка"]
    box.showerror("Ошибка", err[ind])
    
# Начало - создание окна
window = tk.Tk()
window.geometry("400x100")
window.resizable(width=False, height=True)
window.title("Lab-3")

# Создание лейблов и полей ввода для:
# 1) Ввод
entry_in = tk.Entry(window)
entry_in.grid(row=2, column=0, stick="w")
lb_in = tk.Label(window, text="Input:")
lb_in.grid(row=1, column=0, stick="w")
# 2) Вывод
entry_out = tk.Entry(window)
entry_out.grid(row=2, column=1, stick="w")
lb_out = tk.Label(window, text="Output:")
lb_out.grid(row=1, column=1, stick="w")
# 3) Название картинки
entry_p = tk.Entry(window)
entry_p.grid(row=2, column=2, stick="w")
lb_p = tk.Label(window, text="Save Image Name:")
lb_p.grid(row=1, column=2, stick="w")

# Кнопка зашифровывания
startButton = tk.Button(text="Зашифровать", command=encode)
startButton.grid(row=0, column=0, stick="wens")
# Кнопка расшифровывания
startButton = tk.Button(text="Расшифровать", command=decode)
startButton.grid(row=0, column=1, stick="wens")

window.mainloop()
