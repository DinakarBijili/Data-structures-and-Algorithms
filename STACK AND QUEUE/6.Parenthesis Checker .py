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
def Parenthesis_checker(exp):
    dict = {"{":"}",'(':')',"[":"]"}
    stack = []
    for c in exp:
        if c in dict.keys():
            stack.append(c)
        elif c in dict.values():
            if not stack:
                return False
            last = stack.pop()
            if dict[last] != c:
                return False 
    if stack:
        return False
    return True
    
if __name__ == "__main__":
    exp = "("
    print(Parenthesis_checker(exp))
    