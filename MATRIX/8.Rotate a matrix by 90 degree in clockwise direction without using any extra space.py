"""
Rotate a matrix by 90 degree in clockwise direction without using any extra space

Given a square matrix, turn it by 90 degrees in a clockwise direction without using any extra space.

Examples: 

Input:
1 2 3 
4 5 6
7 8 9  
Output:
7 4 1 
8 5 2
9 6 3

Input:
1 2
3 4
Output:
3 1
4 2 

"""
def rotate_matrix(matrix, N):
    for i in range(N):
        for j in range(i):
            matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]

    
    #Swap columns
    for i in range(N):
        for j in range(N//2):
            matrix[i][j], matrix[i][N-j-1] =matrix[i][N-j-1] , matrix[i][j]
    


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4 ,5, 6],
              [7 ,8 ,9]]
    N = len(matrix)
    result = (rotate_matrix(matrix, N))
    for i in range(N):
        print(matrix[i])
    