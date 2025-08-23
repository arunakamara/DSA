def decimal_to_binary(num):
    assert isinstance(num, int), "The parameter must be an integer only."
    if num == 0:
        return 0
    
    else:
        return num%2 + 10 * decimal_to_binary(num//2)



print(decimal_to_binary(10))