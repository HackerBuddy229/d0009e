import math


def tvarsumman2(n):
    if n == 0:
        return n
    
    length = int(math.log10(n)) + 1

    total = 0

    for i in range(length):
        if i == 0:
            current_number = n
        else:
            current_number = n // 10**i

        total = total + (current_number % 10)

    return total

