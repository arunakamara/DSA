from sum_of_digits import sum_of_digits

def digital_root(num):
    if num < 10:
        return num
    return digital_root(sum_of_digits(num))

print(digital_root(9875))


#################################################################
#################################################################


def digital_root(num):
    while num >= 10:
        num = sum_of_digits(num)
    return num

print(digital_root(9875))  # Output: 2


#################################################################
#################################################################


def digital_root_recursive(num):
    if num < 10:   # already a single digit
        return num
    return digital_root_recursive(sum(map(int, str(num))))

print(digital_root_recursive(9875))  # Output: 2


#################################################################
#################################################################


def digital_root_iterative(num):
    while num >= 10:   # repeat until single digit
        num = sum(map(int, str(num)))
    return num

print(digital_root_iterative(9875))  # Output: 2


#################################################################
#################################################################

def digital_root_math(num):
    """
    Time Complexity - O(1) 
    """
    if num == 0:
        return 0
    return 9 if num % 9 == 0 else num % 9

print(digital_root_math(9875))  # Output: 2

