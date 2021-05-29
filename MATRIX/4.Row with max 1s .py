"""
Row with max 1s 

Given a boolean 2D array of n x m dimensions where each row is sorted. Find the 0-based index of the first row that has the maximum number of 1's.

Example 1:

Input: 
N = 4 , M = 4
Arr[][] = [[0, 1, 1, 1],
           [0, 0, 1, 1],
           [1, 1, 1, 1],
           [0, 0, 0, 0]]
Output: 2
Explanation: Row 2 contains 4 1's (0-based
indexing).

Example 2:

Input: 
N = 2, M = 2
Arr[][] = [[0, 0], [1, 1]]
Output: 1
Explanation: Row 1 contains 2 1's (0-based
indexing).

"""
def Row_with_max(matrix):
    l = 0
    r = len(matrix[0])-1
    row = -1
    while l <= len(matrix)-1 and r >= 0:
        if matrix[l][r] == 1:
            r -= 1
            row = l # updating row
        else:
            l += 1 # otherwise move down 
            
    return row 

if __name__ == "__main__":
    matrix = [[0, 1, 1, 1],[0, 0, 1, 1],[1, 1, 1, 1],[0, 0, 0, 0]]
    result = Row_with_max(matrix)
    print(result)