def Russian_doll(n):
    if n < 1:
        return 
    
    # Prints in ascending order
    Russian_doll(n-1)
    print(f"Doll No. {n}")
    
    # Prints in descending order
    # print(f"Doll NO. {n}") 
    # Russian_doll(n-1)


def main():
    num = int(input("Enter the number of dolls: "))
    Russian_doll(num)

if __name__ == "__main__":
    main()
