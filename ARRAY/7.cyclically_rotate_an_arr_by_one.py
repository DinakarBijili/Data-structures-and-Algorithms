"""
Cyclically rotate an array by one 

Given an array, rotate the array by one position in clock-wise direction.
 

Example 1:

Input:
N = 5
A[] = {1, 2, 3, 4, 5}
Output:
5 1 2 3 4
 

Example 2:

Input:
N = 8
A[] = {9, 8, 7, 6, 4, 2, 1, 3}
Output:
3 9 8 7 6 4 2 1
 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function rotate() which takes the array A[] and its size N as inputs and modify the array.

 
"""
def rotate(arr):
    last = arr[len(arr)- 1]
    for i in range(len(arr)-1,0,-1):
        arr[i] = arr[i -1]
    arr[0] = last
    return arr


if __name__ == "__main__":
    arr = [1,2,3,4,5]
    print(rotate(arr))