"""
Find a specific pair in Matrix

Given an n x n matrix mat[n][n] of integers, find the maximum value of mat(c, d) – mat(a, b) over all choices of indexes such that both c > a and d > b.
Example: 

Input:
mat[N][N] = {[1, 2, -1, -4, -20 ],
             [-8, -3, 4, 2, 1 ], 
             [3, 8, 6, 1, 3 ],
             [-4, -1, 1, 7, -6 ],
             [0, -4, 10, -5, 1 ];
Output: 18
The maximum value is 18 as mat[4][2] 
- mat[1][0] = 18 has maximum difference. 

"""
def Specific_pair(matrix):
    N = 5
    maxVal = 0
    for a in range(N -1): # except last row
        for b in range(N -1): # repeated 
            for c in range(a + 1 , N):
                for d in range(b + 1, N):
                    if maxVal < int(matrix[c][d] - matrix[a][b]):
                        maxVal = int(matrix[c][d] - matrix[a][b])
    return maxVal
            

if __name__ == "__main__":
    matrix = [[1, 2, -1, -4, -20 ],
             [-8, -3, 4, 2, 1 ], 
             [3, 8, 6, 1, 3 ],
             [-4, -1, 1, 7, -6 ],
             [0, -4, 10, -5, 1 ]]
    print(Specific_pair(matrix))
    
