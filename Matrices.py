
# rows = int(input("rows : "))
# cols = int(input("cols : "))
# matrix = []
# for i in range(rows):
#     a = []
#     for j in range(cols):
#         a.append(int(input()))
#     matrix.append(a)
# ## print(matrix)
# for i in range(rows):
#     for j in range(cols):
#         print(matrix[i][j] , end=" ")
#     print()


# snake formate

# rows = int(input("rows : "))
# cols = int(input("cols : "))
# matrix = []
# for i in range(rows):
#     a = []
#     for j in range(cols):
#         a.append(int(input()))
#     matrix.append(a)
# print(matrix)
#
# for i in range(rows):
#     if(i % 2 == 0):
#         for j in range(cols):
#             print(matrix[i][j],end=" ")
#     else:
#         for j in range(cols-1,-1,-1):
#             print(matrix[i][j] , end=" ")

# printing boundary elements of matrices

# rows = int(input("rows : "))
# cols = int(input("cols : "))
# matrix = []
# for i in range(rows):
#     a = []
#     for j in range(cols):
#         a.append(int(input()))
#     matrix.append(a)
# print(matrix)
# if(rows == 1):
#     for i in range(cols):
#         print(matrix[0][i])
# elif(cols == 1):
#     for j in range(rows):
#         print(matrix[j][0])
#
# else:
#     for j in range(cols):
#         print(matrix[0][j], end=" ")
#
#     for i in range(1, rows):
#         print(matrix[i][cols-1], end=" ")
#
#     for j in range(cols-2, -1, -1):
#         print(matrix[rows-1][j], end=" ")
#
#     for i in range(rows-2, 0, -1):
#         print(matrix[i][0], end=" ")

# transpose of matrix

# rows = int(input("rows : "))
# cols = int(input("cols : "))
# matrix = []
# for i in range(rows):
#     a = []
#     for j in range(cols):
#         a.append(int(input()))
#     matrix.append(a)
# print(matrix)
# transposed_matrix = [[0 for j in range(rows)] for i in range(cols)]
# # print(transposed_matrix)
# for i in range(rows):
#     for j in range(cols):
#         transposed_matrix[i][j] = matrix[j][i]
# print(transposed_matrix)


# rows = int(input("rows : "))
# cols = int(input("cols : "))
# matrix = []
# for i in range(rows):
#     a = []
#     for j in range(cols):
#         a.append(int(input()))
#     matrix.append(a)
# print(matrix)
# for i in range(rows):
#     for j in range(i+1,cols):
#         matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
# print(matrix)

# rotation of matrix in counter clock wise direction

# rows = int(input("rows : "))
# cols = int(input("cols : "))
# matrix = []
# for i in range(rows):
#     a = []
#     for j in range(cols):
#         a.append(int(input()))
#     matrix.append(a)
# print(matrix)
# rotated_matrix = [[0 for j in range(cols)] for i in range(rows)]
# for i in range(rows):
#     for j in range(cols):
#         rotated_matrix[cols -1 - j][i] = matrix[i][j]
# print(rotated_matrix)

# rotation of matrix in clock wise direction

# rows = int(input("rows : "))
# cols = int(input("cols : "))
# matrix = []
# for i in range(rows):
#     a = []
#     for j in range(cols):
#         a.append(int(input()))
#     matrix.append(a)
# print(matrix)
# rotated_matrix = [[0 for j in range(cols)] for i in range(rows)]
# for i in range(rows):
#     for j in range(cols):
#         rotated_matrix[j][rows - 1 - i] = matrix[i][j]
# print(rotated_matrix)

# spiral traversal of a matrix is a way of visiting all the elements of a matrix in a spiral manner

# rows = int(input("rows : "))
# cols = int(input("cols : "))
# matrix = []
# for i in range(rows):
#     a = []
#     for j in range(cols):
#         a.append(int(input()))
#     matrix.append(a)
# print(matrix)
#
# def spiral_traversal(matrix):
#     if not matrix:
#         return []
#     result = []
#     top, bottom = 0, len(matrix) - 1
#     left, right = 0, len(matrix[0]) - 1
#     while top <= bottom and left <= right:
#         for i in range(left, right + 1):
#             result.append(matrix[top][i])
#         top += 1
#         for i in range(top, bottom + 1):
#             result.append(matrix[i][right])
#         right -= 1
#         if top <= bottom:
#             for i in range(right, left - 1, -1):
#                 result.append(matrix[bottom][i])
#         bottom -= 1
#         if left <= right:
#             for i in range(bottom, top - 1, -1):
#                 result.append(matrix[i][left])
#         left += 1
#     return result

# print(spiral_traversal(matrix))


# multiplication of matrices

# rows = int(input("rows : "))
# cols = int(input("cols : "))
# matrix = []
# for i in range(rows):
#     a = []
#     for j in range(cols):
#         a.append(int(input()))
#     matrix.append(a)
# print(matrix)
#
# rows1 = int(input("rows : "))
# cols1 = int(input("cols : "))
# matrix1 = []
# for i in range(rows1):
#     b = []
#     for j in range(cols1):
#         b.append(int(input()))
#     matrix1.append(b)
# print(matrix1)
#
# result = [[0 for j in range(rows)] for i in range(cols1)]
#
# for i in range(len(matrix)):
#     for j in range(len(matrix1[0])):
#         for k in range(len(matrix1)):
#             result[i][j] = matrix[i][k] * matrix1[k][j]
# print(result)


# sum of upper and lower triangle

# rows = int(input("rows : "))
# cols = int(input("cols : "))
# matrix = []
# for i in range(rows):
#     a = []
#     for j in range(cols):
#         a.append(int(input()))
#     matrix.append(a)
# print(matrix)
#
# upper_sum = 0
# lower_sum = 0
#
# for i in range(rows):
#     for j in range(cols):
#         if i < j :
#             upper_sum += matrix[i][j]
#         elif j < i:
#             lower_sum += matrix[i][j]
# print(upper_sum , lower_sum)

# Reversed matrix

# def reverse_columns(matrix):
#     for row in matrix:
#         row.reverse()
#     return matrix
#
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# reversed_matrix = reverse_columns(matrix)
# print("Reversed matrix:")
# for row in reversed_matrix:
#     print(row)


