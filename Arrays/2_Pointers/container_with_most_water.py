def container_with_most_water(heights):
    # Initialize i to the first element in the heights array
    i = 0

    # Initialize j to the last element
    j = len(heights)-1

    # Initialize max_area to 0
    max_area = 0

    # While the pointers have not meet
    while i < j:
        
        width = j - i
        height = min(heights[i], heights[j])
        area = width * height
        max_area = max(max_area, area)

        # We only move on pointer at a time
        # and that is the one with the min value of height
        if (heights[i] < heights[j]):
            i += 1
        else:
            j -= 1

    return max_area 

arr = [1,8,6,2,5,4,8,3,7]
print(container_with_most_water(arr))
