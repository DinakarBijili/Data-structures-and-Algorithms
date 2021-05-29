"""
    Minimize the Heights II 

Given an array arr[] denoting heights of N towers and a positive integer K, you have to modify the height of each tower either by increasing or decreasing them by K only once. After modifying, height should be a non-negative integer. 
Find out what could be the possible minimum difference of the height of shortest and longest towers after you have modified each tower.

A slight modification of the problem can be found here.


Example 1:

Input:
K = 2, N = 4
Arr[] = {1, 5, 8, 10}
Output:
5
Explanation:
The array can be modified as 
{3, 3, 6, 8}. The difference between 
the largest and the smallest is 8-3 = 5.
Example 2:

Input:
K = 3, N = 5
Arr[] = {3, 9, 12, 16, 20}
Output:
11
Explanation:
The array can be modified as
{6, 12, 9, 13, 17}. The difference between 
the largest and the smallest is 17-6 = 11. 

Your Task:
You don't need to read input or print anything. Your task is to complete the function getMinDiff() which takes the arr[], n and k as input parameters and returns an integer denoting the minimum difference.


Expected Time Complexity: O(N*logN)
Expected Auxiliary Space: O(N)
"""

def getMindif(arr,k):

    min_val = [] # 10 10 13 11 9 8 13 14
    max_val = [] # 9 15
    
    for i in range(len(arr)):
        if arr[i] <= 10:
            arr[i] += k 
            min_val.append(arr[i])
            
        else:
            arr[i] -= k 
            max_val.append(arr[i])
            
        print("%45s  %-45s"%(min_val,max_val))
        
        
    maximum = max(max_val)
    
    max_to_min = min(max_val)
    minimum = min(min_val)
    
    if minimum > max_to_min and maximum != max_to_min:
        result =  (maximum - max_to_min)
    else:
        result = (maximum - minimum)

    return result
    
if __name__ == "__main__":
    arr = [5, 5, 8, 6, 4, 10, 3 ,8 ,9, 10] # 10 10 13 11 9 5 8 13 14 15 
    k = 5
    result = getMindif(arr,k)
    print(abs(result))