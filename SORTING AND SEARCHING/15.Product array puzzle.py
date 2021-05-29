"""
Product array puzzle

Given an array nums[] of size n, construct a Product Array P (of same size n) such that P[i] is equal to the product of all the elements of nums except nums[i].

 

Example 1:

Input: nums[] = {10, 3, 5, 6, 2}
Output: 180 600 360 300 900
Explanation: 
For i=0, P[i] = 3*5*6*2 = 180.
For i=1, P[i] = 10*5*6*2 = 600.
For i=2, P[i] = 10*3*6*2 = 360.
For i=3, P[i] = 10*3*5*2 = 300.
For i=4, P[i] = 10*3*5*6 = 900.

Example 2:
Input:
n = 2
nums[] = {12,0}
Output:
0 12

"""
def Produce_arr(nums):
    if len(nums) <= 2:
        return nums
    ans = [a for a in range(len(nums))]
    
    for i in range(len(nums)): # 0 1 2 3 4 
        a = 1
        for j in range(len(nums)): # 0 1 2 3 4 to len of i that means 5 times if i=> 0 j => 0 1 2 3 4 if i => 1 j =>0 1 2 3 4 and so on..
            if i != j: # 0 != 1 
                a = a*nums[j]
            ans[i] = a # 1 3 15 90 180 10 10 50 300 600 10 30 30 180 360 10 30 150 300 10 30 150 300
    return ans

if __name__ == "__main__":
    nums = [10, 3, 5, 6, 2]
    print(Produce_arr(nums)) # 180 600 360 300 900