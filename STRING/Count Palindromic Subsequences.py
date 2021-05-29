"""
Count Palindromic Subsequences 

Given a string str of length N, you have to find number of palindromic subsequence (need not necessarily be distinct) which could be formed from the string str.
Note: You have to return the answer module 109+7;
 

Example 1:

Input: 
Str = "abcd"
Output: 
4
Explanation:
palindromic subsequence are : "a" ,"b", "c" ,"d"
 

Example 2:

Input: 
Str = "aab"
Output: 
4
Explanation:
palindromic subsequence are :"a", "a", "b", "aa"

"""
def Count_Palindromic_subsequences(string):
    count = 0
    for i in range(len(string)):
        for j in range(i + 1, len(string)+1): #1 2 3 4 2 3 4 3 4 4
            temp = string[i:j] # a ab abc abcd b bc bcd c cd d
            if temp == temp[::-1]: # [::-1] -> a ba cba dcba b cb dcb c cd d
                count += 1
    return count
if __name__ == "__main__":
    string = "aaaaaaaaaaaaaaaaaaaaaaaaaaa"
    print(Count_Palindromic_subsequences(string))