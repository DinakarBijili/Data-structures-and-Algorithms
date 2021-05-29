"""
Minimum Swaps to Sort 

Given an array of n distinct elements. Find the minimum number of swaps required to sort the array in strictly increasing order.


Example 1:

Input:
nums = {2, 8, 5, 4}
Output:
1
Explaination:
swap 8 with 4.
Example 2:

Input:
nums = {10, 19, 6, 3, 5}
Output:
2
Explaination:
swap 10 with 3 and swap 19 with 5.

"""
def minimum_swaps_to_sort(nums):
    pass
    # swap = 0
    # for i in range(len(nums)):    
    #     for j in range((nums)):
    #         if nums[j] < nums[i]:
    #             nums[i],nums[j] = nums[j],nums[i]
    #             swap += 1
    # return swap
if __name__ == "__main__":
    nums = [10, 19, 6, 3, 5]
    print(minimum_swaps_to_sort(nums))