"""
Longest Repeating Subsequence 

Given a string str, find length of the longest repeating subseequence such that the two subsequence don’t have same string character at same position, i.e., any i’th character in the two subsequences shouldn’t have the same index in the original string.
 

Exampel 1:

Input: str = "axxxy"
Output: 2
Explanation: The longest repeating subsequenece
is "xx".
Example 2:

Input: str = "aab"
output: 1
Explanation: The longest reapting subsequenece
is "a".

"""
def Longest_repeating_subsequence(string):

    repeated = {}
    for i in string:
        if i in repeated:
            repeated[i] += 1
        else:
            repeated[i] = 1
    for i in repeated.values():
        if i >= 1 :   
            return i
if __name__ == "__main__":
    string = "agcsorvauz"
    print(Longest_repeating_subsequence(string))