import numpy as np

def diagonal_sum(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i][i]
    return sum

matrix = np.array([[1, 2, 3], [2, 2, 5], [4, 6, 3]])
print(matrix)

print(diagonal_sum(matrix))


