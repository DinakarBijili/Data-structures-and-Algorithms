"""
Longest Palindrome in a String

Given a string S, find the longest palindromic substring in S. Substring of string S: S[ i . . . . j ] where 0 ≤ i ≤ j < len(S). Palindrome string: A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S. Incase of conflict, return the substring which occurs first ( with the least starting index).

Example 1:

Input:
S = "aaaabbaa"
Output: aabbaa
Explanation: The longest Palindromic
substring is "aabbaa".
â€‹Example 2:

Input: 
S = "abc"
Output: a
Explanation: "a", "b" and "c" are the 
longest palindromes with same length.
The result is the one with the least
starting index.

Your Task:
You don't need to read input or print anything. Your task is to complete the function longestPalin() which takes the string S as input and returns the longest palindromic substring of S.


"""
def longestPalindrome(A):
    rev = A[::-1]
    print(rev)
    l = len(A)
    
    while True:
        for i in range(len(A)):
            half = int(l / 2)
            left = A[i : i + half]
            right = rev[len(A) - (i + l) : len(A) - (i + l - half)]
            if left == right:
                return A[i:i+l]
        l -= 1
    
if __name__ == "__main__":
    A = "aaaabbaa"
    print(longestPalindrome(A))