def missing_number(arr, n):
    # Calculate the sum of first n natural numbers
    total = n * (n + 1) // 2
    
    # Calculate the sum of numbers in the array
    sum_arr = sum(arr)
    
    # Find the missing number by subtracting sum_arr from total
    missing = total - sum_arr
    
    return missing
 
# Example
print(missing_number([1, 2, 3, 4, 6], 6))

def missing(arr, n):
    """ 
    Returns a list of missing numbers in the array
    """
    return [ i for i in range(1, n+1) if i not in arr ]

print(missing([1, 3, 5, 8, 10], 10))
# def missing_number(arr, n):
#     """
#     Returns the missing number in a given array 
#     """
#     for i in range(1, n+1):
#         if i not in arr:
#             return i
    
    
        
        


