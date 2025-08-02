def find_max_avg(arr, k):
    """
    Returns the max average for subarray of length k
    Time Complexity - O(n)
    Space Complexity - O(1)
    """
    # Convert the given array into a prefix_sum array
    for i in range(1, len(arr)):
        arr[i] += arr[i-1]

    # Initialize max sum to the value of the prefix_sum at index k-1 (zero-based index)
    max_sum = arr[k-1]

    # Loop through the array from the next element after the max_sum in the prefix_sum array
    for i in range(k, len(arr)):
        
        # Find the current sum by subtracting the sum before the k_sub_array from the sum at i
        curr_sum = arr[i] - arr[i-k]

        # Update the max_sum value
        max_sum = max(max_sum, curr_sum)
    
    # return the average by dividing by k
    return max_sum / k

arr = [1, 12, -5, -6, 50, 3]
k = 4
print(find_max_avg(arr, k))



    