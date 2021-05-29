"""
Maximum Rectangular Area in a Histogram

Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of contiguous bars. For simplicity, assume that all bars have the same width and the width is 1 unit.

Example 1:

Input:
N = 7
arr[] = {6,2,5,4,5,1,6}
Output: 12
Explanation: 


Example 2:

Input:
N = 8
arr[] = {7 2 8 9 1 3 6 5}
Output: 16
Explanation: Maximum size of the histogram 
will be 8  and there will be 2 consecutive 
histogram. And hence the area of the 
histogram will be 8x2 = 16.

    6          MAX    6
    |     5   / 5     |
    |     |_ 4 _|     |
    |     |  |  |     |
    |  2  |  |  |     |
    |  |  |  |  |  1  |
    |__|__|__|__|__|__|___

"""
def getMaxArea(arr):
    pass


if __name__ == "__main__":
    arr = [6, 2, 5, 4, 5, 1, 6]
    print(getMaxArea(arr))