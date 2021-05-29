"""
Middle of Three

Given three distinct numbers A, B and C. Find the number with value in middle (Try to do it with minimum comparisons).


Example 1:

Input:
A = 978, B = 518, C = 300
Output:
518
Explanation:
Since 518>300 and 518<978, so 
518 is the middle element.

Example 2:

Input:
A = 162, B = 934, C = 200
Output:
200
Exaplanation:
Since 200>162 && 200<934,
So, 200 is the middle element.

Your Task:
You don't need to read input or print anything.Your task is to complete the function middle() which takes three integers A,B and C as input parameters and returns the number which has middle value.

"""
def Find_middle_val(A,B,C):
    if A > B:
        if A < C:
            median = A
        elif B > C:
            median = B
        else:
            median = C
    else: 
        if A > C:
            median = A
        elif B < C:
            median = B
        else:
            median = C
    return median
    
if __name__ == "__main__":
    A = 978
    B = 515
    C = 300
    res = Find_middle_val(A,B,C)
    print("Middle Value is",res)