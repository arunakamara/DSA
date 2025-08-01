def range_sum(arr: list[int], queries: list[tuple]) -> list[int]:
    """
    Returns a list of the inclusive sum of the elements in the range given in each tuple of the queries parameter
    Time Complexity - O(n)
    Space Complexity - O(n)
    """

    # Return an empty list if any of the inputs is empty
    if len(arr) == 0 or len(queries) == 0:
        return []
    
    # Convert input arr into a prefix_sum array
    for i in range(1, len(arr)):
        arr[i] += arr[i-1]

    # Initialize result to empty list
    result = []

    # Loop through the array of tuples
    for i, j in queries:
        if j >= len(arr):
            raise ValueError
        if i == 0:
            result.append(arr[j])
        else:
            result.append(arr[j] - arr[i-1])
    
    return result


arr = [2, 4, 1, 3, 5]
queries = [(1, 3), (0, 4)]
ranges = range_sum(arr, queries)
print(ranges)