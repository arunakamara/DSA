def find_max_num(arr, n):
    if n == 1:
        return arr[0]
    
    return max(arr[n-1], find_max_num(arr, n-1))


def main():
    n = int(input("Enter length of array: "))
    arr = [None] * n
    i = 0
    while True:
        if i == n: break
        arr[i] = int(input((f"Enter element at index {i}: ")))
        i += 1
    
    print(find_max_num(arr, n))


if __name__ == "__main__":
    main()