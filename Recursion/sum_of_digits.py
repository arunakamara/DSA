

def sum_of_digits(num):
    """
    Returns the sum of the individual digits
    """

    if num < 10:
        return num
    
    return (num % 10) + sum_of_digits(num // 10)


def sum_digit_iterative(num):
    # Initialize total 
    total = 0

    while num > 0:
        total += num%10 # Add the last digit to total
        num //= 10      # Remove the last digit from the number
    
    return total

def sum_of_digits_pythonic(num):
    return sum(map(int, str(num)))




def main():
    n = int(input("Enter a number: "))
    digit_sum = sum_of_digits(n)
    print(digit_sum)

if __name__ == "__main__":
    main()