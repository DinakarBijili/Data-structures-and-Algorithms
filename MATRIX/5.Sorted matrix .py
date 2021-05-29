"""
Sorted matrix 
Basic Accuracy: 81.37% Submissions: 4313 Points: 1
Given an NxN matrix Mat. Sort all elements of the matrix.

Example 1:

Input:
N=4
Mat=[[10,20,30,40],
[15,25,35,45] 
[27,29,37,48] 
[32,33,39,50]]
Output:
10 15 20 25 
27 29 30 32
33 35 37 39
40 45 48 50
Explanation:
Sorting the matrix gives this result.
Example 2:

Input:
N=3
Mat=[[1,5,3],[2,8,7],[4,6,9]]
Output:
1 2 3 
4 5 6
7 8 9
Explanation:
Sorting the matrix gives this result.
"""
def Sorted_matrix(matrix, r, c):
    temp = [0] * (r*c)
    
    k  = 0 
    for i in range(0, r):
        for j in range(0, c):
            temp[k] = matrix[i][j]
            
            k+= 1
    temp.sort()
    print("SORTED MATRIX: ",temp)
    
            

if __name__ == "__main__":
    matrix = [[10,20,30,40],[15,25,35,45] ,[27,29,37,48] ,[32,33,39,50]]
    r = 4
    c = 4
    result = Sorted_matrix(matrix,r,c)
    for i in range(0, r):
        for j in range(0, c):
            print(matrix[i][j], end=" ")
        print()
   