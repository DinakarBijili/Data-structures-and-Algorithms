"""
Parenthesis Checker 

Given an expression string x. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
For example, the function should return 'true' for exp = “[()]{}{[()()]()}” and 'false' for exp = “[(])”.

Example 1:

Input:
{([])}
Output: 
true
Explanation: 
{ ( [ ] ) }. Same colored brackets can form 
balaced pairs, with 0 number of 
unbalanced bracket.
Example 2:

Input: 
()
Output: 
true
Explanation: 
(). Same bracket can form balanced pairs, 
and here only 1 type of bracket is 
present and in balanced way.

"""
def parenthesis_check(parenthesis):
    braces = {"{": "}", "(": ")", "[": "]"}
    stack = []
    
    for i in parenthesis:
        if i in braces.keys():
            stack.append(i)
    
        elif i in braces.values():
            if not stack:
                return False
            
            last_brace = stack.pop()
            if braces[last_brace] != i:
                return False

    if stack:
        return False
    return True
if __name__ == "__main__":
    # Parenthesis = input()
    Parenthesis = "[({[([{}])]})}"
    # Parenthesis = "[]"
    
    print(parenthesis_check(Parenthesis))