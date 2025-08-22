def recursive(n):
    if n<1:
        print("n is less than 1")
    else:
        recursive(n-1)
        print(n)


recursive(5)