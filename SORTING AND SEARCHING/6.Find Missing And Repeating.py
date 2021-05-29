"""
Find Missing And Repeating

Given an unsorted array Arr of size N of positive integers. One number 'A' from set {1, 2, …N} is missing and one number 'B' occurs twice in array. Find these two numbers.

Example 1:

Input:
N = 2
Arr[] = {2, 2}
Output: 2 1
Explanation: Repeating number is 2 and 
smallest positive missing number is 1.
Example 2:

Input:
N = 3
Arr[] = {1, 3, 3}
Output: 3 2
Explanation: Repeating number is 3 and 
smallest positive missing number is 2.

"""
def Find_Missing_and_Repeating(arr):
    Repeated = 0
    missing = 0
    val = []
    arr.sort()
    print("sorted list : ",arr)
    for i, j in  enumerate(arr):
        if i+1 not in arr:
            missing = i+1 #missing
        if j not in val:
            val.append(j) 
        else:
            Repeated = j # repeated 
        
    return ("Repeated =",Repeated," missing =", missing)
            
    
if __name__ == "__main__":
    # arr = [1,3,3,4,4]
    arr = [2, 21, 17, 16, 22, 3, 9, 10, 14, 12, 20, 11, 6, 4, 8, 7, 23, 15, 18, 13, 1, 10, 19]
    res = Find_Missing_and_Repeating(arr)
    print(*res) 