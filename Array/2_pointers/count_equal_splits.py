def count_equal_splits(arr):
    """
    Return the number of times the given array can be split into two equal sums
    Time Complexity - O(n)
    Space Complexity - O(1)
    """

    # Initialize total the sum of all elements in the array
    total = sum(arr)

    # Initialize both p_sum and count to 0
    p_sum, count = 0, 0

    # Loop through the array from its first to its second to last element
    for i in range(len(arr) - 1):
        
        # Increment p_sum by the elements in the index
        p_sum += arr[i]

        # If the sum of the visited elements equal to the sum of the remaining elements
        # increment count
        if p_sum == total - p_sum:
            count += 1
        
    return count

arr = [1, 2, 3]
print(count_equal_splits(arr))