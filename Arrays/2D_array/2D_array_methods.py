from create_2D_array import TwoD_array
import numpy as np

def insert(arr, index, data, axis):
    return np.insert(arr, index, data, axis)

def main():
    arr = TwoD_array
    index = int(input("Enter index: "))
    axis = int(input("Enter axis: "))
    data = list(map(int, input("Enter data: ").split()))
    if (axis == 0 and len(data) != len(arr[0])) or (axis == 1 and len(data) != len(arr)):
        raise ValueError(f"Invalid number of data entered. \nPlease enter a data of length {len(arr[0]) if axis == 0 else len(arr) }")
    new_array = insert(arr, index, data, axis)
    print(new_array)


if __name__ == "__main__":
    main()
    

