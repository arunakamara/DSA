def move_zeros(arr):
    i, j = 0, 0

    while j < len(arr) - 1:
        if arr[j] == 0:
            j += 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
    return arr


print(move_zeros([0, 1, 2, 0, 1, 0]))