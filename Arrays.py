'''
🔹 Basic Level (using Python’s array module)
- Create an array of integers and:
- Print the first, last, and middle element.
- Find the length of the array without using len().
- Write a program to insert a new element at the end and at a specific index.
- Remove an element from the array without using remove() or pop().
- Find the maximum and minimum element in an array manually.
- Reverse an array without using slicing.

🔹 Intermediate Level
- Given an array of integers, separate them into even and odd arrays.
- Rotate an array by k positions (e.g., [1,2,3,4,5] rotated by 2 → [4,5,1,2,3]).
- Write a program to merge two arrays into one sorted array.
- Implement a program to find the second largest and second smallest element.
- Write a program to check if an array is palindromic.

🔹 Advanced Level (NumPy arrays)
- Create a 2D NumPy array and:
- Print its shape, size, and dimensions.
- Access a specific row and column.
- Perform matrix addition, subtraction, and multiplication using NumPy arrays.
- Write a program to find the transpose and inverse of a matrix.
- Implement a program to calculate the dot product and cross product of two arrays.
- Given a NumPy array, find all elements greater than a threshold (e.g., > 10).
- Solve the Sudoku validation problem using arrays (check rows, columns, and 3×3 subgrids). '''

# Create an array of integers and: - Print the first, last, and middle element.

import array as arr
arr = [1,2,3,4,5,6,7,8,9,10]
first_element = print(f"First element: {arr[0]}")
middle_element = print(f"Middle element: {arr[len(arr)//2]}")
last_element = print(f"Last element: {arr[-1]}")

# Find the length of the array without using len().
length = 0
for _ in arr:
    length +=1
print(f"Length of the array: {length}")

# Write a program to insert a new element at the end and at a specific index.
new_element = 11
arr.append(new_element)
print(f"Array after inserting at the end: {arr}")
arr.insert(5,12)
print(f"Array after inserting at index 5: {arr}")

# Remove an element from the array without using remove() or pop().
element_remove = 3
new_arr = []
for i in arr:
    if i != element_remove:
        new_arr.append(i)
print(f"Array after removing element {element_remove}: {new_arr}")

# Find the maximum and minimum element in an array manually.
max_element = arr[0]
min_element = arr[0]
for i in arr:
    if i > max_element:
        max_element = i
    if i <  min_element:
        min_element = i
print(f"Maximum element: {max_element}")
print(f"Minimum element: {min_element}")

# Reverse an array without using slicing.
reversed_arr = []
for i in arr:
    reversed_arr = [i]+ reversed_arr
print(f'Reversed array: {reversed_arr}')
print(f"slicing reversed array: {arr[::-1]}")

# Given an array of integers, separate them into even and odd arrays.
def even_odd_array(even_arr , odd_arr):
    for i in arr:
        if i% 2 ==0:
            even_arr.append(i)
        else:
            odd_arr.append(i)
even_arr = []
odd_arr = []
even_odd_array(even_arr=even_arr, odd_arr=odd_arr)
print(f"Even array: {even_arr}")
print(f"Odd array: {odd_arr}")

# Rotate an array by k positions (e.g., [1,2,3,4,5] rotated by 2 → [4,5,1,2,3]).
def rotate_array(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]
arr = [1,2,3,4,5]
k = 2
rotated = rotate_array(arr, k)
print(f"Array after rotating by {k} positions: {rotated}")

# Write a program to merge two arrays into one sorted array.
def merge_sorted_arrays(arr1, arr2):
    merged = arr1 + arr2
    merged.sort()
    return merged
arr1 = [1,3,5]
arr2 = [2,4,6]
merged_array = merge_sorted_arrays(arr1, arr2)
print(f"Merged and sorted array: {merged_array}")

# Implement a program to find the second largest and second smallest element.

# arr = [1,2,3,4,5,6,7,8, 9,10]
# second_largest = arr[-2]
# second_smallest = arr[1]
# print(f"Second largest element: {second_largest}")
# print(f"Second smallest element: {second_smallest}")

def second_largest_smallest(arr):
    unique_arr = list(set(arr))
    unique_arr.sort()
    if len(unique_arr) < 2:
        return "Array does not have enough unique elements."
    second_largest = unique_arr[-2]
    second_smallest = unique_arr[1]
    return second_largest, second_smallest
arr = [1,2,3,4,5,6,7,8, 9,10]
second_largest, second_smallest = second_largest_smallest(arr)
print(f"Second largest element: {second_largest}")
print(f"Second smallest element: {second_smallest}")

# Write a program to check if an array is palindromic.
def is_palindromic(arr):
    return arr == arr[::-1]
arr1 = [1,2,3,2,1]
arr2 = [1,2,3,4,5]
print(f"Is arr1 palindromic? {is_palindromic(arr1)}")
print(f"Is arr2 palindromic? {is_palindromic(arr2)}")

# Create a 2D NumPy array and: - Print its shape, size, and dimensions.
import numpy as np
arr_2d = np.array([[1,2,3],[4,5,6]])
print(f"shape of an array: {arr_2d.shape}")
print(f"size of  an array: {arr_2d.size}")
print(f"dimensions of an array: {arr_2d.ndim}")

# Access a specific row and column.
print(f"first row: {arr_2d[0]}")
print(f"second column: {arr_2d[:,1]}")

# Perform matrix addition, subtraction, and multiplication using NumPy arrays.
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])
print(f"Matrix operation addition: {arr1 + arr2}")
print(f"Matrix operation subtraction: {arr1 - arr2}")
print(f"Matrix operation multiplication: {arr1 * arr2}")

# Write a program to find the transpose and inverse of a matrix.
arr = np.array([[1,2],[3,4]])
transpose = arr.T
inverse = np.linalg.inv(arr)
print(f"Transpose of the matrix: \n{transpose}")
print(f"Inverse of the matrix: \n{inverse}")

# Implement a program to calculate the dot product and cross product of two arrays.
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
dot_product = np.dot(arr1, arr2)
cross_product = np.cross(arr1, arr2)
print(f"Dot product: {dot_product}")
print(f"Cross product: {cross_product}")

# Given a NumPy array, find all elements greater than a threshold (e.g., > 10).
arr = np.array([5,10,15,20,25])
threshold = 10
greater_than_threshold = arr[arr>threshold]
print(f"Elements greater than {threshold}: {greater_than_threshold}")

# Solve the Sudoku validation problem using arrays (check rows, columns, and 3×3 subgrids).
def is_valid_sudoku(board):
    for i in range(9):
        row = set()
        column = set()
        subgrid = set()
        for j in range(9):
            if board[i][j] !='.':
                if board[i][j] in row:
                    return False
                row.add(board[i][j])
                if board[j][i] !='.':
                    if board[j][i] in column:
                        return False
                    column.add(board[j][i])
                    if board[3*(i//3)+j//3][3*(i%3)+j%3] != '.':
                        if board[3*(i//3)+j//3][3*(i%3)+j%3] in subgrid:
                            return False
                        subgrid.add(board[3*(i//3)+j//3][3*(i%3)+j%3])
                    return True
sudoku_board = [
                        ["5","3",".",".","7",".",".",".","."],
                        ["6",".",".","1","9","5",".",".","."],
                        [".","9","8",".",".",".",".","6","."],
                        ["8",".",".",".","6",".",".",".","3"],
                        ["4",".",".","8",".","3",".",".","1"],
                        ["7",".",".",".","2",".",".",".","6"],
                        [".","6",".",".",".",".","2","8","."],
                        [".",".",".","4","1","9",".",".","5"],
                        [".",".",".",".","8",".",".","7","9"]
                    ]
print(f"Is the Sudoku board valid? {is_valid_sudoku(sudoku_board)}")
