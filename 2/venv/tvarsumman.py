import math


def tvärsumman(number):
    length = int(math.log10(number)) + 1
    if length == 1:
        return number

    next_integer = number // 10
    current_integer = (number % 10)

    return tvärsumman(next_integer) + current_integer


print(tvärsumman(1234))
