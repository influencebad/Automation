def square(s):
    print("Площадь квадрата равна: " + str(s))

import math

side = input("Введите сторону квадрата: ")
side =  float(side)

side= math.ceil(side)

s = side * side

square(s)