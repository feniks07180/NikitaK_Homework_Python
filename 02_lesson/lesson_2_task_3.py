from math import ceil

def square(side):
    return ceil(side * side )

side = float(input("Введите размер стороны: "))
print(f"площадь квадрата: {square(side)}")


