"""
Kth smallest element 

Given an array arr[] and a number K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.

Example 1:
Input:
N = 6
arr[] = 7 10 4 3 20 15
K = 3
Output : 7
Explanation :
3rd smallest element in the given 
array is 7.

Example 2:

Input:
N = 5
arr[] = 7 10 4 20 15
K = 4
Output : 15
Explanation :
4th smallest element in the given 
array is 15.
"""
def kth_smallest_element(arr,k):
    arr.sort()
    for i in range(len(arr)):
        if i == k-1:
            return arr[i]
    return None

if __name__ == "__main__":
    arr = [7,10, 4, 3, 20, 15]
    k = 3
    result = kth_smallest_element(arr,k)
    print(k,"smallest element in the given array is",result)