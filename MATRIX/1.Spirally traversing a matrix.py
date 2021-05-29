"""
Spirally traversing a matrix

Given a matrix of size r*c. Traverse the matrix in spiral form.

Example 1:

Input:
r = 4, c = 4
matrix[][] = {{1, 2,  3,  4}, 
             {5,  6,  7,  8},
             {9,  10, 11, 12},
             {13, 14, 15, 16}}
Output: 
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
Explanation:

Example 2:

Input:
r = 3, c = 4  
matrix[][] = {{1, 2, 3, 4},
             {5, 6, 7, 8},
             {9, 10, 11, 12}}
Output: 
1 2 3 4 8 12 11 10 9 5 6 7
Explanation:
Applying same technique as shown above, 
output for the 2nd testcase will be 
1 2 3 4 8 12 11 10 9 5 6 7.

Your Task:
You dont need to read input or print anything. Complete the function spirallyTraverse() that takes matrix, r and c as input parameters and returns a list of integers denoting the spiral traversal of matrix. 
"""

def Spirally_traversing(matrix, top, bottom, left, right):
        # if left > right:
        #     return

        # Print top row
        for i in range(left, right + 1): # TOP ORDER
            print(matrix[top][i],end=" ") #1 2 3 4 5 

        top = top + 1
        
        # if top > bottom:
        #     return 

        #print right column
        for i in range(top, bottom + 1):
            print(matrix[i][right],end=" ")

        right = right -1
        
        # if left > right:
        #     return
        # print Bottom row
        for i in range(right,left-1,-1):
            print(matrix[bottom][i],end=" ")

        bottom = bottom -1
        # if top > bottom:
        #     return

        # print left row
        for i in range(bottom, top-1,-1):
            print(matrix[i][left], end=" ")

        left = left + 1

        Spirally_traversing(matrix, top , bottom, left,right)
if __name__ == "__main__":

    matrix = [
        [1, 2, 3, 4, 5],
        [16, 17, 18, 19, 6],
        [15, 24, 25, 20, 7],
        [14, 23, 22, 21, 8],
        [13, 12, 11, 10, 9]
    ]
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

 
    Spirally_traversing(matrix, top, bottom, left, right)
    
 
    # FOR USER 
    # for _ in range(int(input("ENTER RANGE: "))):
    #     h,w = map(int, input().strip().split())
    #     values = list(map(int, input().strip().split()))
    #     k = 0
    #     matrix = []
    #     for i in range(h):
    #         row =[]
    #         for j in range(w):
    #             row.append(values[k])
    #             k += 1
    #         matrix.append(row)
    #     obj = soluation()
    #     ans = obj.Spirally_traversing(matrix,h,w)
    #     for i in ans:
    #         print(i, end=" ")
    #     print()

        


