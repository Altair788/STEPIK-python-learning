def get_circle(radius):
    from math import pi
    return float(2 * pi * radius), float(pi * (radius ** 2))


r = float(input())

lenght, square = get_circle(r)
print(lenght, square)