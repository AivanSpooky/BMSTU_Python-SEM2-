from tkinter import *
from math import sqrt

class GraphicManager:
    def check_coords(self, x,y):
        try:
            y = float(x)
            y = float(y)
            if x > 500 or x < 0 or y > 500 or y < 0:
                return False
            return True
        except:
            return False
    def add_point(self, x,y):
        if not self.check_coords(x,y) or [x,y] in self.points:
            return
        self.points.append([x,y])
        self.canvas.create_oval(x, y, x + 2, y + 2, fill='blue')
    def distance(self, p1, p2):
        return sqrt( (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def calculate(self):
        min_point = None
        points_ranges = []
        for i in range(len(self.points)):
            max_range = 0
            for j in range(len(self.points)):
                if i != j:
                    if self.distance(self.points[i], self.points[j]) > max_range:
                        max_range = self.distance(self.points[i], self.points[j])
            points_ranges.append(max_range)
        min_range = min(points_ranges)
        min_point = self.points[points_ranges.index(min_range)]
        self.canvas.create_oval(min_point[0] - min_range,
                                min_point[1] - min_range,
                                min_point[0] + min_range,
                                min_point[1] + min_range)

    def __init__(self) -> None:
        self.window = Tk()

        self.x_input_label = Label(self.window, text="x: ")
        self.x_input_label.grid(row=0, column=0)
        self.x_input_entry = Entry(self.window)
        self.x_input_entry.grid(row=0, column=1)

        self.y_input_label = Label(self.window, text="y: ")
        self.y_input_label.grid(row=1, column=0)
        self.y_input_entry = Entry(self.window)
        self.y_input_entry.grid(row=1, column=1)

        self.add_point_button = Button(self.window, text="Добавить", 
                                       command=lambda:self.add_point(self.x_input_entry.get(),self.x_input_entry.get()))
        self.canvas = Canvas(self.window, width=500, height=500, background="white")
        self.canvas.grid(row=2, column=0, columnspan=2)
        self.canvas.bind("<Button-1>", lambda event: self.add_point(event.x, event.y))
        self.points = []

        self.calculate_button = Button(self.window, text="Рассчитать", command=lambda:self.calculate())
        self.calculate_button.grid(row=4, columnspan=2)
        self.x_out_label = Label(self.window, text="")
        self.x_out_label.grid(row=5, column=0)
        self.y_out_label = Label(self.window, text="")
        self.y_out_label.grid(row=5, column=1)

        self.window.mainloop()

GraphicManager()