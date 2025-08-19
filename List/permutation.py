from collections import Counter
def main():
    print(is_permutation([1,2,5,4,3], [1,2,4,6,5]))
    print(Counter([1, 2, 32, 1, 1, 2, 2, 3, 3, 2, 2]))

        
def is_permutation(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    
    return lst1.sort() == lst2.sort()

if __name__ == "__main__":
    main()