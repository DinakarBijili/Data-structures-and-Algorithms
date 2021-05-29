"""
Search a 2D Matrix
Medium

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

"""
def Search_2D_matrix(matrix, target):
    try:
        l = 0 
        r = len(matrix[0])-1
        while True:
            if matrix[l][r] == target:
                return True

            elif matrix[l][r] > target:
                r -= 1
                continue 
            l += 1  
    except:
        return False
        


if __name__ == "__main__":
    matrix =  [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 2
    result = Search_2D_matrix(matrix,target)
    print(result)