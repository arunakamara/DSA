
# def max_product(arr):
#     m1 = arr.pop(arr.index(max(arr))) #------> O(n) because of max() method
#     m2 = arr.pop(arr.index(max(arr))) #------> O(n)
#     return m1 * m2

def max_product(arr):
    max1, max2 = 0, 0

    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num

        elif num > max2:
            max2 = num

    return max1 * max2
    
print(max_product([1, 7, 3, 4, 9, 5]))
