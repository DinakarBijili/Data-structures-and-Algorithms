"""
Rearrange array in alternating positive & negative items with O(1) extra space | Set 1

Given an array of positive and negative numbers,
arrange them in an alternate fashion such that every positive number is followed by negative and vice-versa maintaining the order of appearance. 
Number of positive and negative numbers need not be equal. If there are more positive numbers they appear at the end of the array. If there are more negative numbers, they too appear in the end of the array.

Examples : 

Input:  arr[] = {1, 2, 3, -4, -1, 4}
Output: arr[] = {-4, 1, -1, 2, 3, 4}

Input:  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}


Naive Approach : 
The above problem can be easily solved if O(n) extra space is allowed. It becomes interesting due to the limitations that O(1) extra space and order of appearances. 
The idea is to process array from left to right. While processing, find the first out of place element in the remaining unprocessed array. An element is out of place if it is negative and at odd index, or it is positive and at even index. Once we find an out of place element, we find the first element after it with opposite sign. We right rotate the subarray between these two elements (including these two).

"""
def partition(arr):

    j = 0
    pivot = 0 #consider 0 as a pivot

    #each time we find a negative number j is increamented
    #and a negative elemenet would be placed before the pivot
    for i in range(len(arr)):
        if arr[i] < pivot: # here pivot is 0
            
            #swap arr[i] with arr[j]
            arr[i],arr[j] = arr[j],arr[i]
            j = j + 1
    return j

# Function to rearrange a given list such that it contains positive
# and negative numbers at alternate positions
def rearrange(arr):

    # partition a given list such that all positive elements move
    # to the end of the list

    p = partition(arr) 

       # swap alternate negative elements from the next available positive
    # element till the end of the list is reached or all negative or
    # positive elements are exhausted.
 
    n =0 
    while len(arr) > p > n:
        arr[n],arr[p] = arr[p],arr[n]

        p = p + 1
        n = n + 2

    return arr


if __name__ == "__main__":
    arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
    print(rearrange(arr))
