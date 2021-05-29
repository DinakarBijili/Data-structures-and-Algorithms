"""
Zero Sum Subarrays

You are given an array arr[] of size n. Find the total count of sub-arrays having their sum equal to 0.


Example 1:

Input:
n = 6
arr[] = {0,0,5,5,0,0}
Output: 6
Explanation: The 6 subarrays are 
[0], [0], [0], [0], [0,0], and [0,0].

Example 2:

Input:
n = 10
arr[] = {6,-1,-3,4,-2,2,4,6,-12,-7}
Output: 4
Explanation: The 4 subarrays are [-1 -3 4]
[-2 2], [2 4 6 -12], and [-1 -3 4 -2 2]

"""
# Approach 1: Using Brute-Force

def sum_zero(arr):
    count = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i,len(arr)):
            sum += arr[j]
            # print("sum",sum)
            if sum == 0:
                count += 1
                if count <= 0:
                    return []
    return count
if __name__ == "__main__":
    arr = [6,-1,-3,4,-2,2,4,6,-12,-7]
    res = (sum_zero(arr))
    print("Count:",res)