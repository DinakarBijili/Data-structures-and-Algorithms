"""
Minimum number of jumps 

Given an array of integers where each element represents the max number of steps that can be made forward from that element. Find the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then you cannot move through that element.

Example 1:

Input:
N=11 
arr=1 3 5 8 9 2 6 7 6 8 9 
Output: 3 
Explanation: 
First jump from 1st element to 2nd 
element with value 3. Now, from here 
we jump to 5th element with value 9, 
and from here we will jump to last. 

Example 2:

Input :
N= 6
arr= 1 4 3 2 6 7
Output: 2 
Explanation: 
First we jump from the 1st to 2nd element 
and then jump to the last element.
Your task:
You don't need to read input or print anything. Your task is to complete function minJumps() which takes the array arr and it's size N as input parameters and returns the minimum number of jumps.

Expected Time Complexity: O(N)
Expected Space Complexity: O(1)
"""


def jump(arr):
        if len(arr) <= 1 : 
            return 0 
  
        # Return -1 if not possible to jump 
        if arr[0] <= 0 :  
            return -1 

        jump_count = 0
        curr_reachable = 0
        for index , values in enumerate(arr):
            
            if index > curr_reachable: 
                curr_reachable = reachable
                jump_count += 1

            reachable = max(0,index + values) 
            
        return jump_count

if __name__ == "__main__":
    arr =   [1,3, 5, 8, 9, 2, 6, 7, 6, 8, 9 ]
    # ndex =[0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    result = jump(arr)
    print("Max Jumps to reach End in",result,"Steps!")