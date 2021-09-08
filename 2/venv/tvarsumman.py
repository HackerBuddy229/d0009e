import math


def tvarsumman(number):
    length = int(math.log10(number)) + 1
    if length == 1:
        return number

    next_integer = number // 10
    current_integer = (number % 10)

    return tvarsumman(next_integer) + current_integer


print(tvarsumman(1234))
