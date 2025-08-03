def move_zeros(arr):
    """
    Returns an the same array with all 0's being at the end
    Time Complexity - O(n)
    Space Complexity - O(1)
    """

    # Initialize two pointers i and j to the first element
    i, j = 0, 0

    # Loop pointer j from 0 to the end of the list
    while j < len(arr) - 1:

        # Keep moving j forward if the element is 0
        if arr[j] == 0:
            j += 1

        else:

            # If the element at index j is not 0, swap with element at index i and increment both i and j
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
    return arr


print(move_zeros([0, 1, 2, 0, 1, 0]))