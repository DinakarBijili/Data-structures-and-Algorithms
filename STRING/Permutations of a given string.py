"""
Permutations of a given string 

Given a string S. The task is to print all permutations of a given string.

Example 1:

Input: ABC
Output:
ABC ACB BAC BCA CAB CBA
Explanation:
Given string ABC has permutations in 6 
forms as ABC, ACB, BAC, BCA, CAB and CBA .
Example 2:

Input: ABSG
Output:
ABGS ABSG AGBS AGSB ASBG ASGB BAGS 
BASG BGAS BGSA BSAG BSGA GABS GASB 
GBAS GBSA GSAB GSBA SABG SAGB SBAG 
SBGA SGAB SGBA
Explanation:
Given string ABSG has 24 permutations.

"""

def permutations(string):
    permutations_list = []
    if len(string) == 1:
        return string
    else:
        for char in string:
            [permutations_list.append(char + a) for a in permutations(string.replace(char, "", 1))]

    return permutations_list

if __name__ == "__main__":
    string = "ABC"
    print(permutations(string))