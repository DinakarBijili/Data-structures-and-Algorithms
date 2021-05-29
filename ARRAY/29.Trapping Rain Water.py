"""
Trapping Rain Water 

Given an array arr[] of N non-negative integers representing the height of blocks. If width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 
 
Example 1:

Input:
N = 6
arr[] = {3,0,0,2,0,4}
Output:
10
Explanation: 

Example 2:

Input:
N = 4
arr[] = {7,4,0,9}
Output:
10
Explanation:
Water trapped by above 
block of height 4 is 3 units and above 
block of height 0 is 7 units. So, the 
total unit of water trapped is 10 units.
Example 3:

Input:
N = 3
arr[] = {6,9,9}
Output:
0
Explanation:
No water will be trapped.

Your Task:
You don'y need to read input or print anything. The task is to complete the function trappingWater() which takes arr and N as input parameters and returns the total amount of water that can be trapped.
"""
def Tapping_water(heights):
    result = 0
    left = 0 
    right = len(heights)-1
    level = 0

    while left < right:                   
        if heights[left] < heights[right]:
            lower = heights[left] # finds the lower between right and left
            left += 1
        else:
            lower = heights[right]
            right -= 1
            
        level = max(level , lower)
        result += level - lower # 3-3 =0 ,3-0 = 3, 3-0 = 3 ,3-2 = 1, 3-0 = 3 = 10

    return result


if __name__ == "__main__":
    heights = [3,0,0,2,0,4]
    result = Tapping_water(heights)
    print(result)
