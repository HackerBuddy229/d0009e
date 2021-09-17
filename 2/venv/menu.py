import bounce
import bounce2
import solve
import tvarsumman
import tvarsumman2


class ExitState:
    exit = True


def do_exit(n):
    return ExitState()


options = {
    1: bounce.bounce,
    2: bounce2.bounce,
    3: tvarsumman.tvarsumman,
    4: tvarsumman2.tvarsumman2,
    5: do_exit
}


def present_menu():
    print("""
    1 = bounce
    2 = bounce 2
    3 = tvärsumma
    4 = tvärsumma 2
    5 = exit
    """)


def handle_input(input) -> int:
    try:
        result = options[int(input)](23)

    except IndexError:
        return -1

    if isinstance(result, ExitState):
        return 0
    else:
        return 1


def get_input():
    user_input = input()
    return user_input


while True:
    present_menu()
    user_input = get_input()
    result = handle_input(user_input)
    if result == 0:
        break

