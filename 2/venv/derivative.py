import math


def derivative(f, x, h):
    kvot = 1/(2*h)
    f_positive = f(x+h)
    f_negative = f(x - h)

    result = kvot*(f_positive-f_negative)
    return result


print(derivative(math.cos, math.pi, 0.0001))
print(derivative(math.sin, math.pi, 0.0001))
print(derivative(math.tan, math.pi, 0.0001))