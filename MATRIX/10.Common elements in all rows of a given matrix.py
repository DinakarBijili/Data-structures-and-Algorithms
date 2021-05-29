"""
Common elements in all rows of a given matrix

Given an m x n matrix, find all common elements present in all rows in O(mn) time and one traversal of matrix.
Example: 

Input:
mat[4][5] = [[1, 2, 1, 4, 8],
             [3, 7, 8, 5, 1],
             [8, 7, 7, 3, 1],
             [8, 1, 2, 7, 9],
            ];

Output: 
1 8 or 8 1
8 and 1 are present in all rows.

"""
def Common_elements(matrix, r, c):
    res = list(set.intersection(*map(set, matrix)))
    return res


if __name__ == "__main__":
    matrix = [[1, 2, 1, 4, 8],
             [3, 7, 8, 5, 1],
             [8, 7, 7, 3, 1],
             [8, 1, 2, 7, 9]]

    r = 4
    c = 5
    result = Common_elements(matrix, r, c)
    print(* result)
