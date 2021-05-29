"""
Count pairs with given sum 

Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.


Example 1:

Input:
N = 4, K = 6
arr[] = {1, 5, 7, 1}
Output: 2
Explanation: 
arr[0] + arr[1] = 1 + 5 = 6 
and arr[1] + arr[3] = 5 + 1 = 6.

Example 2:

Input:
N = 4, X = 2
arr[] = {1, 1, 1, 1}
Output: 6
Explanation: 
Each 1 will produce sum 2 with any 1.

Your Task:
You don't need to read input or print anything. 
Your task is to complete the function getPairsCount() which takes arr[], n and k as input parameters and returns the number of pairs that have sum K.

"""
def pairs(arr,k):
    if not arr:
        return []
    count = 0
    # consider each element except the last
    for i in range(len(arr)-1): 

        # start from the i'th element until the last element
        for j in range(i + 1, len(arr)):

              # if the desired sum is found, print it
            if arr[i] + arr[j] == k:
                print("pair FOund",arr[i],arr[j])
                count += 1
        
        return count

if __name__ == "__main__":
    arr = [1, 5, 7, 1]
    k = 6
    print(pairs(arr,k))