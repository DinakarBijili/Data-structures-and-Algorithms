"""
Longest consecutive subsequence 

Given an array of positive integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.
 

Example 1:

Input:
N = 7
a[] = {2,6,1,9,4,5,3}
Output:
6
Explanation:
The consecutive numbers here
are 1, 2, 3, 4, 5, 6. These 6 
numbers form the longest consecutive
subsquence.
Example 2:

Input:
N = 7
a[] = {1,9,3,10,4,20,2}
Output:
4
Explanation:
1, 2, 3, 4 is the longest
consecutive subsequence.

Your Task:
You don't need to read input or print anything. 
Your task is to complete the function findLongestConseqSubseq() which takes the array arr[] and the size of the array as inputs and returns the length of the longest subsequence of consecutive integers. 

"""
def Longest_sunsequence(arr):
    arr.sort()
    print(arr)
    for i , j in enumerate(arr):
        if j <= i + 1:
            global res
            res = j 
    return res

if __name__ == "__main__":
    arr = [9,8, 7, 6, 5, 4, 9, 8, 7, 6, 5, 4, 4]
    result = Longest_sunsequence(arr)
    print("Longest_subsequence:",result)