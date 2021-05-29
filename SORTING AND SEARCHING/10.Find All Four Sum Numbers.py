"""
Find All Four Sum Numbers

Given an array of integers and another number. Find all the unique quadruple from the given array that sums up to the given number.

Example 1:

Input:
N = 5, K = 3
A[] = {0,0,2,1,1}
Output: 0 0 1 2 $
Explanation: Sum of 0, 0, 1, 2 is equal
to K.
Example 2:

Input:
N = 7, K = 23
A[] = {10,2,3,4,5,7,8}
Output: 2 3 8 10 $2 4 7 10 $3 5 7 8 $
Explanation: Sum of 2, 3, 8, 10 = 23,
sum of 2, 4, 7, 10 = 23 and sum of 3,
5, 7, 8 = 23.

Your Task:
You don't need to read input or print anything. Your task is to complete the function fourSum() which takes the array arr[] and the integer k as its input and returns an array containing all the quadruples in a lexicographical manner. Also note that all the quadruples should be internally sorted, ie for any quadruple [q1, q2, q3, q4] the following should follow: q1 <= q2 <= q3 <= q4.  (In the output each quadruple is separate by $. The printing is done by the driver's code)

Expected Time Complexity: O(N3).
"""
def Find_Four_sun(arr,k):
    if len(arr) <  4:
        return []

    
    ans = []
    arr.sort()
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            for a in range(j+1, len(arr)):
                for b in range(a+1, len(arr)):
                    if arr[i] +arr[j] +arr[a]+arr[b] == k:
                        ans.append([arr[i],arr[j],arr[a],arr[b]])
                        
    return ans

if __name__ == "__main__":
    arr = [10,2,3,4,5,7,8]
    k = 23
    res = (Find_Four_sun(arr,k))
    for i in res:
        for j in i:
            print(j, end=" ")
        print("$",end="")

