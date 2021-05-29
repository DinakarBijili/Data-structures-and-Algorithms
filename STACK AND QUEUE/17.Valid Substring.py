"""
Valid Substring

Given a string S consisting only of opening and closing parenthesis 'ie '('  and ')', find out the length of the longest valid(well-formed) parentheses substring.
NOTE: Length of smallest the valid substring ( ) is 2.

Example 1:

Input: S = "(()("
Output: 2
Explanation: The longest valid 
substring is "()". Length = 2.
Example 2:

Input: S = "()(())("
Output: 6
Explanation: The longest valid 
substring is "()(())". Length = 6.

"""
def Valid_SubString(s):
    if not s:
        return []
    stack = []
    count = 0
    for char in s:
        if char:
            while "(" == ")" :
                count += 1
            return count
        # if char != ")":
        #     stack.append(char)
        # else:
        #     while char[-1] != "(":
        #         count += 2
        #         break
                
    # return count

if __name__=="__main__":
    # s = "()(())("
    s = '()'
    # s = '))()(()'
    # s = '(((()'
    # s = '((()))'
    print(Valid_SubString(s))