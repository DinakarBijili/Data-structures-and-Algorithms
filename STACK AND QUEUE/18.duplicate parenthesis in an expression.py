"""
Expression contains redundant bracket or not


Given a string of balanced expression, find if it contains a redundant parenthesis or not. A set of parenthesis are redundant if same sub-expression is surrounded by unnecessary or multiple brackets. Print ‘Yes’ if redundant else ‘No’.
Note: Expression may contain ‘+‘, ‘*‘, ‘–‘ and ‘/‘ operators. Given expression is valid and there are no white spaces present.
Example: 
 

Input: 
((a+b))
(a+(b)/c)
(a+b*(c-d))
Output: 
Yes
Yes
No

Explanation:
1. ((a+b)) can reduced to (a+b), this Redundant
2. (a+(b)/c) can reduced to (a+b/c) because b is
surrounded by () which is redundant.
3. (a+b*(c-d)) doesn't have any redundant or multiple
brackets.

"""
def duplicate_parenthesis(exp):
    if len(exp) <= 3:
        return False
    stack = []

    for char in exp:    
        #appends opening '('
        if char != ")":
            stack.append(char)
        else:
            # if last value is equal to '('
            if stack[-1] == "(":
                return True
             # pop till `(` is found for current `)`
            #  ['(', '(', 'x', '+']
            #  ['(', '(', 'x']
            #  ['(', '(']    
            while stack[-1] != "(":
                stack.pop()
                # print(stack) -> check out 
            #pop '('
            stack.pop()
            # print(stack) -> check out 
    # if we reach here, then the expression does not have any
    # duplicate parenthesis
    return False



if __name__ == "__main__":
    # exp = "((x+y))" 
    exp = "((x+y)+((z)))" 
    if duplicate_parenthesis(exp):
        print("yes exp has duplicate parenthesis")
    else:
        print("No exp does not have duplicate parenthesis")
