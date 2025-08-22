def power_of_2_iteration(n):

    if n < 0:
        return f"Please enter a positive value."
    i = 0
    power = 1

    while i < n:
        power *= 2
        i += 1
    return power


def power_of_2_recursive(n):

    if n < 0:
        return f"Please enter a positive value."

    if n == 0:
        return 1
    if n == 1:
        return 2

    return power_of_2_recursive(n-1) * 2 


def main():
    n = int(input("Enter n value: "))
    iterative_power = power_of_2_iteration(n)
    recursive_power = power_of_2_recursive(n)
    print(f"Iterative Power: {iterative_power}")
    print(f"Recursive Power: {recursive_power}")
    

if __name__ == "__main__":
    main()