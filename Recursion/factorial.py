def factorial(n):
    assert n >= 0 and isinstance(n, int), "Please enter a positive integer."
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n-1)

def factorial_iteration(n):
    fact = 1
    i = 1
    while i <= n:
        fact *= i
        i += 1
    return fact


def main():
    n = int(input("Enter n: "))
    fact = factorial(n)
    print(f"Recursive Factorial: {fact}")
    fact_iteration = factorial_iteration(n)
    print(f"Iterative Factorial: {fact_iteration}")


if __name__ == "__main__":
    main()

