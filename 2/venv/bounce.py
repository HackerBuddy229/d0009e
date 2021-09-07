
def bounce(n, has_hit_zero=False, current_index=-1):
    if n == current_index:
        return

    if not has_hit_zero:
        if current_index != -1:
            print(current_index)
            if current_index == 0:
                bounce(n, True, 0)
            else:
                bounce(n, False, current_index-1)
        else:
            print(n)
            bounce(n, False, n-1)
    else:
        print(current_index+1)
        bounce(n, True, current_index+1)


