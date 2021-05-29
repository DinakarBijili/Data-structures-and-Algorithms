"""
Kth element in Matrix 

Given a N x N matrix, where every row and column is sorted in non-decreasing order. Find the kth smallest element in the matrix.

Example 1:
Input:
N = 4
mat[][] =     [[16, 28, 60, 64],
                   [22, 41, 63, 91],
                   [27, 50, 87, 93],
                   [36, 78, 87, 94 ]]
K = 3
Output: 27
Explanation: 27 is the 3rd smallest element.
 

Example 2:
Input:
N = 4
mat[][] =     [[10, 20, 30, 40]
                   [15, 25, 35, 45]
                   [24, 29, 37, 48]
                   [32, 33, 39, 50]]
K = 7
Output: 30
Explanation: 30 is the 7th smallest element.


Your Task:
You don't need to read input or print anything. Complete the function kthsmallest() which takes the mat, N and K as input parameters and returns the kth smallest element in the matrix.

"""
def Kth_element(matrix, k , N):
    temp = [0] * N*N
    a = 0
    for i in range(N):
        for j in range(N):
            temp[a] = matrix[i][j]
            a += 1
            print(a, end=" ")
    print("\n")
    print("BEFORE SORTING: ", temp)
    temp.sort()
    print("SORTED MATRIX: ",temp)
    for i in range(len(temp)):
        if i + 1 == k :
            return temp[i]

    

if __name__ == "__main__":
    matrix = [[16, 28, 60, 64],
                   [22, 41, 63, 91],
                   [27, 50, 87, 93],
                   [36, 78, 87, 94 ]]
    k = 3
    N = len(matrix)
    result = Kth_element(matrix, k, N)
    print("Kth_element: ",result)