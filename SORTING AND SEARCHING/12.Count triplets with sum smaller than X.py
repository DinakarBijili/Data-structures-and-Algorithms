"""
Count triplets with sum smaller than X

Given an array arr[] of distinct integers of size N and a sum value X, the task is to find count of triplets with the sum smaller than the given sum value X.

Example 1:

Input: N = 6, X = 2
arr[] = {-2, 0, 1, 3}
Output:  2
Explanation: Below are triplets with 
sum less than 2 (-2, 0, 1) and (-2, 0, 3). 

Example 2:

Input: N = 5, X = 12
arr[] = {5, 1, 3, 4, 7}
Output: 4
Explanation: Below are triplets with 
sum less than 12 (1, 3, 4), (1, 3, 5), 
(1, 3, 7) and (1, 4, 5).


Your Task:
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function countTriplets() that take array arr[], integer N  and integer X as parameters and returns the count of triplets.

"""

def Count_triples_sum_less_than_k(arr, f):
    count = 0
    arr.sort()
    for i in range(len(arr)-1):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1,len(arr)):
                if arr[i]+arr[j]+arr[k] < f:
                    # ans.append([arr[i],arr[j],arr[k]])
                    count += 1
                    if count <=0 :
                        return 0
    return count

if __name__ == "__main__":
    arr = [5, 1, 3, 4, 7]
    f = 12
    res = Count_triples_sum_less_than_k(arr, f)
    print(res)