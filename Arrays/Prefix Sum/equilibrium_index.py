def equilibrium_index(arr):
    """
    Return the index where sum of all elements on the left equals to sum of all elements to the right
    Time Complexity - O(n)
    Space Complexity - O(1)
    """

    # Initialize left_sum as 0
    left_sum = 0

    # Calculate the total sum
    total = sum(arr)

    # Loop through the arr 
    for i in range(len(arr)):

        # Sum of elements at the right equal to total sum minus sum of elements on the left
        # But since it's a strict equilibrium we subtract the element at the index also
        right_sum = total - left_sum - arr[i]

        # If both sums are equal return the index
        if left_sum == right_sum:
            return i
        
        # Increment the left_sum by adding the current element to it
        left_sum += arr[i]
        
    # Return -1 if there is no such index
    return -1

arr = [1, 3, 5, 2, 2]
print(equilibrium_index(arr))

