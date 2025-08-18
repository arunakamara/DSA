from create_2D_array import TwoD_array
import numpy as np

# Insert Method
def insert(arr, index=0, data=[], axis=0):
    """
    Adds a new row or a new column to the array
    Time Complexity - O(mn)
    Space Complexity - O(mn)
    """
    index = int(input("Enter index: "))
    axis = int(input("Enter axis: "))
    data = list(map(int, input("Enter data: ").split()))
    if (axis == 0 and len(data) != len(arr[0])) or (axis == 1 and len(data) != len(arr)):
        raise ValueError(f"Invalid number of data entered. \nPlease enter a data of length {len(arr[0]) if axis == 0 else len(arr) }")
    return np.insert(arr, index, data, axis)



# Access Method
def accessElement(arr):
    """
    Returns the element at the given indices
    Time Complexity - O(1)
    Space Complexity - O(1)
    """
    rowIndex = int(input("Enter the row index: "))
    colIndex = int(input("Enter the column index: "))

    if rowIndex >= len(arr) or colIndex >= len(arr[0]):
        return f"Invalid Index"
    return arr[rowIndex][colIndex]


def traverse(arr):
    """
    Time Complexity - O(mn)
    Space Complexity - O(1)
    """
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print("  ", end="")
    return

def search(arr, value):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == value:
                return f"The value is located at {i}, {j}"
    return f"The element is not found."


def main():
    arr = TwoD_array
    # new_array = insert(arr)

    # print(arr, end="\n\n")

    # element = accessElement(arr)
    # print(element)

    # traverse(arr)

    print(search(arr, 2))


if __name__ == "__main__":
    main()
    

