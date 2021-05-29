"""
Subarray with 0 sum 

Given an array of positive and negative numbers. Find if there is a subarray (of size at-least one) with 0 sum.

Example 1:

Input:
4 2 -3 1 6
Output: 
Yes
Explanation: 
2, -3, 1 is the subarray 
with sum 0.

Example 2:

Input:
5
4 2 0 1 6

Output: 
Yes

Explanation: 
0 is one of the element 
in the array so there exist a 
subarray with sum 0.
Your Task:
You only need to complete the function subArrayExists() that takes array and n as parameters and returns true or false depending upon whether there is a subarray present with 0-sum or not. Printing will be taken care by the drivers code.
"""

def Find_sum_equal_to_0(nums):
    sum =0
    s = set()
    s.add(0)
    
    for i in nums:
        sum += i # Adds total
        
        if sum in s:
            return True
            
        s.add(i)
            
    return False
            

if __name__ =="__main__":
    nums = [4,2,-3,1,6]
    print(Find_sum_equal_to_0(nums))

    