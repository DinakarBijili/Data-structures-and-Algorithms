"""
Find Pair Given Difference

Given an array Arr[] of size L and a number N, you need to write a program to find if there exists a pair of elements in the array whose difference is N.

Example 1:

Input:
L = 6, N = 78
arr[] = {5, 20, 3, 2, 5, 80}
Output: 1
Explanation: (2, 80) have difference of 78.

Example 2:
Input:
L = 5, N = 45
arr[] = {90, 70, 20, 80, 50}
Output: -1
Explanation: There is no pair with difference of 45.

"""
def Find_pairs(arr,n):
    if not arr:
        return None
    count = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if (arr[j]-arr[i]) == n:
                print(arr[j],"-",arr[i])
                count += 1
                if count <= 0:
                    return -1
    return count



if __name__ == "__main__":
    arr = [5, 20, 3, 2, 5, 80]
    n = 78
    print(Find_pairs(arr,n))