"""
Kadane's Algorithm 

Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

Example 1:

Input:
N = 5
arr[] = {1,2,3,-2,5}
Output:
9
Explanation:
Max subarray sum is 9
of elements (1, 2, 3, -2, 5) which 
is a contiguous subarray.
Example 2:

Input:
N = 4
arr[] = {-1,-2,-3,-4}
Output:
-1
Explanation:
Max subarray sum is -1 
of element (-1)
 

Your Task:
You don't need to read input or print anything. The task is to complete the function maxSubarraySum() which takes arr and N as input parameters and returns the sum of subarray with maximum sum.

 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)


"""
def max_sum_subarray(arr):
    
    max_so_far = arr[0]
    curr_max = arr[0]
    
    for i in range(1, len(arr)):
        curr_max = max(arr[i],curr_max + arr[i])
        max_so_far = max(max_so_far,curr_max)

    return max_so_far

if __name__ == "__main__":
    # arr = [1,2,3,-2,5]
    arr = [74,-72, 94, -53, -59, -3, -66, 36, -13, 22, 73, 15 ,-52, 75]
    result = max_sum_subarray(arr)
    print(result)