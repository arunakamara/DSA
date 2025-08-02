def subarray_sum(arr, k):
    """
    Returns the number of subarrays whose sum is equal to k
    Time Complexity - O(n)
    Space Complexity - O(n)
    """

    # Initialize prefix_sum and count to zero
    p_sum, count = 0, 0

    # Use a hashmap / dictionary to keep track of prefix sum
    # Were keys equal to prefix sum and values equal to their frequency
    # Initial as below because prefix sum is initially 0
    # This also ensure that if the first occurring element is equal to k it will be accounted for
    freq = {0: 1}

    # Loop through the array adding its elements to prefix sum
    for num in arr:
        p_sum += num

        # Increment count by the difference of prefix sum and k if such value is in the dictionary
        count += freq.get(p_sum - k, 0)

        # Increment the value of the prefix sum by 1 in the dictionary if it exist else add it their with value of 1
        freq[p_sum] = freq.get(p_sum, 0) + 1
    return count

#=========================================================#
#--------------------------ALTERNATIVELY------------------#
#=========================================================#

def sub_array_sum(arr, k):
    count, p_sum = 0, 0
    dict = {0: 1}

    for num in arr:
        p_sum += num

        if (p_sum - k) in dict:
            count += dict[p_sum - k]
        
        if p_sum in dict:
            dict[p_sum] += 1
        else:
            dict[p_sum] = 1
    return count

arr = [1,2,3]
k = 3
print(sub_array_sum(arr, k)) 

    