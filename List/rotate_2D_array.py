# def rotate(matrix):
#     n = len(matrix)
    
#     for i in range(n):
#         for j in range(i, n):
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
#     for row in matrix:
#         row.reverse()
#     return matrix

def rotate(matrix):
    n = len(matrix)

    print(matrix)

    transposed = [list(row) for row in zip(*matrix)]

    print(transposed)
    
    for row in transposed:
        row.reverse()
    return transposed        
print(rotate( [[1,2,3],[4,5,6],[7,8,9]]))