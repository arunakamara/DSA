def power(base, exp):
    assert  isinstance(exp, int), "The exponent must be integer only"
    # assert num > 0 and exp > 0  and isinstance(num, int), "The number should be a positive integer."

    if exp == 0:
        return 1
    
    elif exp < 0:
        return 1 / (base * power(base, exp+1))  
    
    return base * power(base, exp-1)


print(power(-2.3, -1))