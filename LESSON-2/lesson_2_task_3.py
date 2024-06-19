import math


def square(s):
    print("Площадь квадрата равна: " + str(s))


side = input("Введите сторону квадрата: ")
side =  float(side)

s = side * side
s = math.ceil(s)

square(s)
