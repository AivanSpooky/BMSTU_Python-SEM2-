# Смирнов Иван ИУ7-22Б Лабораторная работа №4 Вариант 17
from tkinter import *
from tkinter.ttk import Treeview
from funcs import *
        
class Graphic_manager:
    def check_coords(self,x,y):
        try:
            if float(x) < 0 or float(x) > 500:
                return False
            elif float(y) < 0 or float(y) > 500:
                return False
            return True
        except:
            return False
    def clear_points(self):
        self.canvas.delete(ALL)
        self.points = []
        for point in self.points_table.get_children():
            self.points_table.delete(point)
        for point in self.min_table.get_children():
            self.min_table.delete(point)
    def add_point(self):
        x = self.x_input_entry.get()
        y = self.y_input_entry.get()
        if self.check_coords(x,y):
            x = float(x)
            y = float(y)
            if [x,y] in self.points:
                print("Уже есть такая точка")
                return
            self.points.append([x,y])
            self.canvas.create_oval(x, y, x + 2, y + 2, fill='blue')
            self.points_table.insert("", "end", text="1", values=(x,y))
        else:
            print("Неверно заданы точки")
    def add_point_coords(self, x,y):
        if self.check_coords(x,y):
            x = float(x)
            y = float(y)
            if [x,y] in self.points:
                print("Уже есть такая точка")
                return
            self.points.append([x,y])
            self.canvas.create_oval(x, y, x + 2, y + 2, fill='blue')
            self.points_table.insert("", "end", text="1", values=(x,y))
        else:
            print("Неверно заданы точки")
    def calculate(self):
        if len(self.points) < 3:
            print("Слишком мало точек (< 3)")
        min_bis_points = define_right_triangle(self.points)
        if len(min_bis_points) == 0:
            print("Невозможно построить ни один треугольник")
            return
        
        self.canvas.delete(ALL)
        for i in self.points:
            x = i[0]
            y = i[1]
            self.canvas.create_oval(x, y, x + 2, y + 2, fill='blue')

        self.canvas.create_line(*min_bis_points[0], *min_bis_points[1], fill="red")
        self.canvas.create_line(*min_bis_points[1], *min_bis_points[2], fill="red")
        self.canvas.create_line(*min_bis_points[2], *min_bis_points[0], fill="red")
        for point in self.min_table.get_children():
            self.min_table.delete(point)
        for i, (x, y) in enumerate(min_bis_points):
            self.min_table.insert(parent='', index=i, iid=i, values=(x, y))

    def callback(self, event):
        self.add_point_coords(event.x, event.y)
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("lab_4")

        self.points = []

        self.x_input_label = Label(self.window, text="x:")
        self.x_input_label.grid(row=0, column=0)
        self.x_input_entry = Entry(self.window, width=30)
        self.x_input_entry.grid(row=0, column=1)

        self.y_input_label = Label(self.window, text="y:")
        self.y_input_label.grid(row=1, column=0)
        self.y_input_entry = Entry(self.window, width=30)
        self.y_input_entry.grid(row=1, column=1)

        self.add_point_button = Button(self.window, text = "Добавить", command=lambda:self.add_point())
        self.add_point_button.grid(row=0, column=2)

        self.clear_button = Button(self.window, text = "Очистить", command=lambda:self.clear_points() )
        self.clear_button.grid(row=1, column=2)

        self.calculate_button = Button(self.window, text = "Раcсчитать",command=lambda:self.calculate())
        self.calculate_button.grid(row=2, rowspan=1, column=0, columnspan=2)

        self.canvas = Canvas(self.window, width=500, height=500)
        self.canvas.grid(row=3, column=1, columnspan=3)
        self.canvas.configure(background='white')
        self.canvas.bind("<Button-1>", lambda event: self.add_point_coords(event.x, event.y))

        self.paints_table_label = Label(self.window, text="Точки")
        self.paints_table_label.grid(row=2, column=0)
        self.points_table = Treeview(self.window)
        self.points_table.grid(row=3,rowspan=1, column = 0)
        self.points_table["columns"] = ("x", "y")
        self.points_table.column("#0", width=0, stretch=False)
        self.points_table.column("x", width=50, minwidth=25)
        self.points_table.column("y", width=50, minwidth=25)
        self.points_table.configure(height = 24)
        self.points_table.heading("x", text="X")
        self.points_table.heading("y", text="Y")

        self.min_table_label = Label(self.window, text="Вершины полученного треугольника")
        self.min_table_label.grid(row=4, column=0, columnspan=5)
        self.min_table = Treeview(self.window)
        self.min_table.grid(row=5, column = 0, columnspan=5)
        self.min_table["columns"] = ("x", "y")
        self.min_table.column("#0", width=0, stretch=False)
        self.min_table.column("x", anchor="w", width=300, minwidth=100)
        self.min_table.column("y", anchor="w", width=300, minwidth=100)

        self.min_table.heading("x", text="X")
        self.min_table.heading("y", text="Y")
        self.min_table.configure(height=3)

        self.window.mainloop()
Graphic_manager()
# paints_table_label = Label(window, text="Точки")
# paints_table_label.grid(row=3, column=0)
# points_table = Treeview(window)
# points_table.grid(row=3,rowspan=1, column = 0)
# points_table["columns"] = ("x", "y", "r")
# points_table.column("#0", width=0, stretch=False)
# points_table.column("x", width=50, minwidth=25)
# points_table.column("y", width=50, minwidth=25)
# points_table.column("r", width=50, minwidth=25)
# points_table.configure(height = 24)
# points_table.heading("x", text="X")
# points_table.heading("y", text="Y")
# points_table.heading("r", text="R")