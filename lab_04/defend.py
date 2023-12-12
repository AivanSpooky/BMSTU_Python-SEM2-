from tkinter import *
from math import sqrt

def distance(p1, p2):
    return sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def calculate():
    if len(points) < 1:
        print("Слишком мало точек (< 1)")
    ##
    eps = 1e-10
    max_counter = -1
    right_circle = []
    for p in points:
        counter = 0
        for pi in points:
            if distance(p, pi) - (pi[2] + p[2]) <= eps:
                counter += 1
        if counter > max_counter:
            max_counter = counter
            right_circle = p
    ##
    canvas.delete(ALL)
    for point in points:
        if point == right_circle:
            canvas.create_oval(point[0]+point[2], point[1]-point[2], point[0]-point[2], point[1]+point[2], fill="red")
        else:
            canvas.create_oval(point[0]+point[2], point[1]-point[2], point[0]-point[2], point[1]+point[2])
    return

def check_coords(x,y,r):
    try:
        if float(x) < 0 or float(x) > 500:
            return False
        elif float(y) < 0 or float(y) > 500:
            return False
        elif float(r) <= 0 or float(r) > 250:
            return False
        return True
    except:
        return False


def add_point():
    x = x_input_entry.get()
    y = y_input_entry.get()
    r = r_input_entry.get()
    if check_coords(x,y,r):
        x = float(x)
        y = float(y)
        r = float(r)
        if [x,y,r] in points:
            print("Уже есть такая точка")
            return
        points.append([x,y,r])
        canvas.create_oval(x+r, y-r, x-r, y+r)
        #points_table.insert("", "end", text="1", values=(x,y,r))
    else:
        print("Неверно заданы точки")


window = Tk()
window.title("lab_4_def")

points = []

x_input_label = Label(window, text="x:")
x_input_label.grid(row=0, column=0)
x_input_entry = Entry(window, width=30)
x_input_entry.grid(row=0, column=1)

y_input_label = Label(window, text="y:")
y_input_label.grid(row=1, column=0)
y_input_entry = Entry(window, width=30)
y_input_entry.grid(row=1, column=1)

r_input_label = Label(window, text="r:")
r_input_label.grid(row=2, column=0)
r_input_entry = Entry(window, width=30)
r_input_entry.grid(row=2, column=1)

add_point_button = Button(window, text = "Добавить", command=lambda:add_point())
add_point_button.grid(row=0, column=3)


calculate_button = Button(window, text = "Раcсчитать",command=lambda:calculate())
calculate_button.grid(row=2, rowspan=1, column=3, columnspan=2)

canvas = Canvas(window, width=500, height=500)
canvas.grid(row=3, column=1, columnspan=3)
canvas.configure(background='white')

window.mainloop()
