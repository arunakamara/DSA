def Russian_doll(n):
    if n < 1:
        return 
    print(f"Doll NO. {n}")
    
    return Russian_doll(n-1)


def main():
    num = int(input("Enter the number of dolls: "))
    Russian_doll(num)

if __name__ == "__main__":
    main()
