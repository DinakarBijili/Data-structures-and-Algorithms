"""
Factorials of large numbers 

Given an integer N, find its factorial.

Example 1:

Input: N = 5
Output: 120
Explanation : 5! = 1*2*3*4*5 = 120

Example 2:

Input: N = 10
Output: 3628800
Explanation :
10! = 1*2*3*4*5*6*7*8*9*10 = 3628800

Your Task:
You don't need to read input or print anything. 
Complete the function factorial() that takes integer N as input
parameter and returns a list of integers denoting the digits that make up the factorial of N.

"""
# Recursive METHOD
def factorial(n):
    if n < 1: 
        return 1

    return (n * factorial(n-1))

if __name__ == "__main__":
    n = 5
    print(factorial(n))


#ITERATIVE METHOD
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * 1
    return fact

if __name__ == "__main__":
    n = 5
    print(factorial(n))
