def subarray_sum(arr, k):
    """
    Returns the number of subarrays whose sum is equal to k
    Time Complexity - O(n)
    Space Complexity - O(1)
    """
    prefix = 0
    count = 0
    freq = {0: 1}

    for num in arr:
        prefix += num

        count += freq.get(prefix - k, 0)

        freq[prefix] = freq.get(prefix, 0) + 1
    return count

    

arr = [1,2,3]
k = 3
print(subarray_sum(arr, k)) 

    