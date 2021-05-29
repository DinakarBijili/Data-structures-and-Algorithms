"""
Evaluation of Postfix Expression

Given string S representing a postfix expression, the task is to evaluate the expression and find the final value. Operators will only include the basic arithmetic operators like *, /, + and -.

 

Example 1:

Input: S = "231*+9-" -> 2*(3+1)-9
Output: -4
Explanation:
After solving the given expression, 
we have -4 as result.
 

Example 2:

Input: S = "123+*8-" -> 1*(2+3) - 8
Output: -3
Explanation:
After solving the given postfix 
expression, we have -3 as result.

Example
Expression No	Infix Notation	Prefix Notation	Postfix Notation
1	a + b	+ a b	a b +
2	(a + b) * c	* + a b c	a b + c *
3	a * (b + c)	* a + b c	a b c + *
4	a / b + c / d	+ / a b / c d	a b / c d / +
5	(a + b) * (c + d)	* + a b + c d	a b + c d + *
6	((a + b) * c) - d	- * + a b c d	a b + c * d -

"""
#using Stack (LIFO)
from collections import deque

def Evaluation_of_postfix(s):
    stack = deque()
    for char in s:
        if char.isdigit(): # numbers
            stack.append(int(char))
        #if not
        else:
            #remove top two elements 
            x = stack.pop()
            y = stack.pop()

            # evaluate the expression `x op y`, and push the
            # result back to the stack
            if char == "+":
                stack.append(y + x)
            elif char == "-":
                stack.append(y-x)
            elif char == "*":
                stack.append(y * x)
            elif char == "/":
                stack.append(y // x)

    # At this point, the stack is left with only one element, i.e.,
    # expression result
    return stack.pop()

    

if __name__ == "__main__":
    s = "123+*"
    print(Evaluation_of_postfix(s))

