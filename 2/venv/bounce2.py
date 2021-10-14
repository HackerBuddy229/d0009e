def bounce(n):

    for i in range((n*2)+1):
        if i <= n:
            print(n-i)
        else:
            print(i-n)
