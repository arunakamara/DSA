

def main():
    myList = [1, 2, 3, 2, 3, 4, 5, 6]
    # print(find_pairs(myList, 6))
    print(twoSum([ 4, 6, 3, 3, 11, 2, 15], 6))


def twoSum(arr, target):
    """
    Returns the indices of the two elements that add up to the target
    """
    seen = {}

    for i, num in enumerate(arr):
        complement = target - num

        # Condition for unique pair
        # if complement in seen and complement != num:

        if complement in seen:
            return seen[complement], i
        seen[num] = i



def find_pairs(arr, target):
    """
    Returns a list of tuples with the indices of all pairs that sum up to the target value
    """
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]: # To avoid adding same pairs to the list
                continue
            elif arr[i] + arr[j] == target:
                pairs.append((i, j))
    return pairs


if __name__ == "__main__":
    main()
    