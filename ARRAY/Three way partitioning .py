"""
Three way partitioning 

Given an array of size n and a range [a, b]. The task is to partition the array around the range such that array is divided into three parts.
1) All elements smaller than a come first.
2) All elements in range a to b come next.
3) All elements greater than b appear in the end.
The individual elements of three sets can appear in any order. You are required to return the modified array.


Example 1:

Input: 
n = 5
A[] = {1, 2, 3, 3, 4}
[a, b] = [1, 2]
Output: 1
Explanation: One possible arrangement is:
{1, 2, 3, 3, 4}. If you return a valid
arrangement, output will be 1.
"""
def Three_way_partitioning(arr, a, b):
    l = 0
    r = len(arr)-1
    s = 0
    while l <= r:
        if arr[l] < a:
            arr[l],arr[s] = arr[s],arr[l]
            l += 1
            s += 1

        elif arr[l] > b:
                arr[l],arr[s] = arr[s],arr[l]
                r -= 1
        else:
            l +=1 
    return arr
if __name__ == "__main__":
    arr = [1,2,3,3,4]
    a = 1
    b = 2
    print(Three_way_partitioning(arr,a,b))
