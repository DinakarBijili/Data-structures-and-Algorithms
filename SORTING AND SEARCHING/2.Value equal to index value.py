"""
Value equal to index value

Given an array Arr of N positive integers. Your task is to find the elements whose value is equal to that of its index value.

Example 1:

Input: 
N = 5
Arr[] = {15, 2, 45, 12, 7}
Output: 2
Explanation: Only Arr[2] = 2 exists here.
Example 2:

Input: 
N = 1
Arr[] = {1}
Output: 1
Explanation: Here Arr[1] = 1 exists.

"""
def Value_equal_to_index(arr):
    mylist = []
    for i, j in enumerate(arr):
        if i+1 == j:
            mylist.append(j)
    if mylist == []:
        return []

    return mylist
if __name__ == "__main__":
    arr = [1]
    res = Value_equal_to_index(arr)
    print(*res)