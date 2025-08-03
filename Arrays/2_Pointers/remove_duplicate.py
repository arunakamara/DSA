def remove_duplicate(arr):
    """
    Input: Sorted array
    Returns the given array with only unique elements
    Time Complexity - O(n)
    Space Complexity - O(1)
    """
    i = 0

    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return arr[:i+1]

arr = [1, 2, 2, 3, 3, 3, 5, 6, 7, 7]
print(remove_duplicate(arr))