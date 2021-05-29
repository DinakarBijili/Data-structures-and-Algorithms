"""
Stickler Thief

Stickler the thief wants to loot money from a society having n houses in a single line. He is a weird person and follows a certain rule when looting the houses. According to the rule, he will never loot two consecutive houses. At the same time, he wants to maximize the amount he loots. The thief knows which house has what amount of money but is unable to come up with an optimal looting strategy. He asks for your help to find the maximum money he can get if he strictly follows the rule. Each house has a[i] amount of money present in it.

Example 1:

Input:
n = 6
a[] = {5,5,10,100,10,5}
Output: 110
Explanation: 5+100+5=110


Example 2:
Input:
n = 3
a[] = {1,2,3}
Output: 4
Explanation: 1+3=4
Your Task:
Complete the function FindMaxSum() which takes an array arr[] and n as input which returns the maximum money he can get following the rules

"""
def Stickler_thief(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    if len(arr) ==2:
        return max(arr[0],arr[1])
    dp = [0]*len(arr)
   
    # Initialize the dp[0] and dp[1]
    dp[0] = arr[0] # 1st val 
    dp[1] = max(arr[0], arr[1]) # 1 and 2 max val 

     
    # Fill remaining positions
    for i in range(2, len(arr)):
        dp[i] = max(arr[i]+dp[i-2], dp[i-1]) # 15 105 105 110
 
    return dp[-1]
if __name__ == "__main__":
    arr = [5,5,10,100,10,5]
    print(Stickler_thief(arr))