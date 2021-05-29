"""
Median in a row-wise sorted Matrix 

Given a row wise sorted matrix of size RxC where R and C are always odd, find the median of the matrix.

Example 1:

Input:
R = 3, C = 3
M = [[1, 3, 5], 
     [2, 6, 9], 
     [3, 6, 9]]

Output: 5

Explanation:
Sorting matrix elements gives us 
{1,2,3,3,5,6,6,9,9}. Hence, 5 is median. 
 

Example 2:

Input:
R = 3, C = 1
M = [[1], [2], [3]]
Output: 2

"""
def median(matrix, r, c):
    temp = [0] * (r*c)
    print(temp)
    k = 0
    for i in range(0, r):
        for j in range(0, c):
            temp[k] = matrix[i][j]

            k +=1
    print("Before sorting: ",temp)
    temp.sort()
    print("After sorting: ",temp)
    l = len(temp)
    median = temp[l//2]

    return median
   
        

if __name__ == "__main__":
    matrix = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]
    r = 3
    c = 3
    result = median(matrix,r,c)
    print("median",result)
