# def remove_duplicate(arr):
#     """
#     Using two pointers - O(n)
#     """


#     i = 0

#     for j in range(1, len(arr)):
#         if arr[i] != arr[j]:
#             i += 1
#             arr[i] = arr[j]
        
#     return arr[:i+1]

def remove_duplicate(lst):
    """Using set"""
    return list(set(lst))
    
arr = [1, 2, 2, 3, 5, 5, 5]
print(remove_duplicate(arr))