import math


def squared(x):
    return x**2-2


def derivative(f, x, h):
    kvot = 1 / (2 * h)
    f_positive = f(x + h)
    f_negative = f(x - h)

    result = kvot * (f_positive - f_negative)
    return result


def solve(f, x0, h):
    x_last = x0
    delta_y_last = 0 - f(x0)

    while True:
        x_current = x_last - (f(x_last) / derivative(f, x_last, h))
        delta_y_current = 0 - f(x_current)

        if abs(delta_y_current - delta_y_last) < h:
            break

        x_last = x_current
        delta_y_last = delta_y_current

    return x_current

