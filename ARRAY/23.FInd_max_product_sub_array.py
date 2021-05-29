"""
Maximum Product Subarray 

Given an array Arr that contains N integers (may be positive, negative or zero). Find the product of the maximum product subarray.

Example 1:

Input:
N = 5
Arr[] = {6, -3, -10, 0, 2}
Output: 180
Explanation: Subarray with maximum product
is  6, -3, -10 which gives product as 180.
Example 2:

Input:
N = 6
Arr[] = {2, 3, 4, 5, -1, 0}
Output: 120
Explanation: Subarray with maximum product
is 2, 3, 4, 5 which gives product as 120.
Your Task:
You don't need to read input or print anything. 
Your task is to complete the function maxProduct() which takes the array of integers arr and n as parameters and returns an integer denoting the answer.

"""
def maxProductSubArray(arr):
    # maintain two variables to store the maximum and minimum product
    # ending at the current index
    max_ending = min_ending = 0
 
    # to store the maximum product sublist found so far
    max_so_far = 0
    print("Visualizing: \n")
    # traverse the given list
    for i in arr:
        temp = max_ending
 
        # update the maximum product ending at the current index
        max_ending = max(i, max(i * max_ending, i * min_ending))
          
        # update the minimum product ending at the current index
        min_ending = min(i, min(i * temp, i * min_ending))
 
        max_so_far = max(max_so_far, max_ending)
    
        print("%2s %5s %5s \n"% (max_ending, min_ending, max_so_far ))

    print("%2s %-5s"% (max_so_far, max_ending))
    return max_so_far


if __name__ == "__main__":
    arr = [6, -3, -10, 0, 2]
    print("%2s"%(arr))
    result = (maxProductSubArray(arr))
    print ("Max Product: ",result)