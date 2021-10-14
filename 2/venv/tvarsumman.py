
def tvarsumman(number):

    if number < 10:
        return number

    next_integer = number // 10
    current_integer = (number % 10)

    return tvarsumman(next_integer) + current_integer
