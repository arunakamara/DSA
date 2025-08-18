from create_2D_array import TwoD_array
import numpy as np

# Insert Method
def insert(arr, index=0, data=[], axis=0):
    index = int(input("Enter index: "))
    axis = int(input("Enter axis: "))
    data = list(map(int, input("Enter data: ").split()))
    if (axis == 0 and len(data) != len(arr[0])) or (axis == 1 and len(data) != len(arr)):
        raise ValueError(f"Invalid number of data entered. \nPlease enter a data of length {len(arr[0]) if axis == 0 else len(arr) }")
    return np.insert(arr, index, data, axis)

# Access Method
def accessElement(arr):
    rowIndex = int(input("Enter the row index: "))
    colIndex = int(input("Enter the column index: "))

    if rowIndex >= len(arr) or colIndex >= len(arr[0]):
        return f"Invalid Index"
    return arr[rowIndex][colIndex]


def main():
    arr = TwoD_array
    # new_array = insert(arr)

    print(arr)

    element = accessElement(arr)
    print(element)


if __name__ == "__main__":
    main()
    

