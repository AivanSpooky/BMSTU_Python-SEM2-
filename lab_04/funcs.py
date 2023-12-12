from math import sqrt
import itertools

# Расстояние между точками
def distance(p1, p2):
    return sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

# Признак на существование треугольника (да/нет)
def can_build_triangle(p1, p2, p3):
    a = distance(p1, p2)
    b = distance(p2, p3)
    c = distance(p1, p3)
    return (a + b > c) and (a + c > b) and (b + c > a)

# Посчитать площадь треугольника
def square(p1, p2, p3):
    a = distance(p1, p2)
    b = distance(p2, p3)
    c = distance(p1, p3)
    p = (a + b + c) / 2
    return sqrt(p*(p-a)*(p-b)*(p-c))

# Найти треугольник, у которого разность между внутреннеми и внешними точками минимальна
def define_right_triangle(points):
    eps = 1e-10
    min_counter = 1e+10
    right_triangle = []
    for p1, p2, p3 in itertools.combinations(points, 3):
        counter = 0
        if not can_build_triangle(p1, p2, p3):
            continue
        for p in points:
            if abs((square(p, p1, p2) + square(p, p2, p3) + square(p, p1, p3)) - square(p1, p2, p3)) < eps:
                counter += 1
            else:
                counter -= 1
        if counter < min_counter:
            min_counter = counter
            right_triangle = [p1, p2, p3]
    return right_triangle
