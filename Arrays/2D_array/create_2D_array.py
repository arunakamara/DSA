import numpy as np


TwoD_array = np.array([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]])

def main():

    print(TwoD_array)

    #Insert a row at index 0
    print(np.insert(TwoD_array, 0, [1, 1, 1, 1], 0))

    print()

    #Insert a column at index 0
    print(np.insert(TwoD_array, 0, [2, 2, 2], 1))

    print()


    #Append a new row
    print(np.append(TwoD_array, [[3, 3, 3, 3]], 0))

    print()

    print(TwoD_array)

    print()

    # #Append a new column
    print(np.append(TwoD_array, np.array([[4, 4, 4]]).reshape(-1, 1), axis=1))  # Use of reshape()
    print(np.append(TwoD_array, np.array[[4], [4], [4]])) # Alternative way

if __name__ == "__main__":
    main()
