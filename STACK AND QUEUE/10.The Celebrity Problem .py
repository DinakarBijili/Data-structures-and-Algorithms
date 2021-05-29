"""
The Celebrity Problem 

A celebrity is a person who is known to all but does not know anyone at a party. If you go to a party of N people, find if there is a celebrity in the party or not.
A square NxN matrix M[][] is used to represent people at the party such that if an element of row i and column j  is set to 1 it means ith person knows jth person. Here M[i][i] will always be 0.
Note: Follow 0 based indexing.
 

Example 1:

Input:
N = 3
M[][] = {{0 1 0},
         {0 0 0}, 
         {0 1 0}}
Output: 1
Explanation: 0th and 2nd person both
know 1. Therefore, 1 is the celebrity. 

Example 2:

Input:
N = 2
M[][] = {{0 1},
         {1 0}}
Output: -1
Explanation: The two people at the party both
know each other. None of them is a celebrity.
"""
# def knows(a, b):
     
#     return matrix[a][b]
 
# # Returns -1 if celebrity
# # is not present. If present,
# # returns id (value from 0 to n-1).
# def findCelebrity(matrix,n):
     
#     # Handle trivial
#     # case of size = 2
#     s = []
 
#     # Push everybody to stack
#     for i in range(n):
#         s.append(i)
 
#     # Extract top 2
#     A = s.pop()
#     B = s.pop()
 
#     # Find a potential celebrity
#     while (len(s) > 1):
#         if (knows(A, B)):
#             A = s.pop()
#         else:
#             B = s.pop()
             
#     # If there are only two people
#     # and there is no
#     # potential candicate
#     if(len(s) == 0):
#         return -1
         
#     # Potential candidate?
#     C = s.pop();
 
#     # Last candidate was not
#     # examined, it leads one
#     # excess comparison (optimize)
#     if (knows(C, B)):
#         C = B
         
#     if (knows(C, A)):
#         C = A
 
#     # Check if C is actually
#     # a celebrity or not
#     for i in range(n):
     
#         # If any person doesn't
#         # know 'a' or 'a' doesn't
#         # know any person, return -1
#         if ((i != C) and
#            (knows(C, i) or
#            not(knows(i, C)))):
#             return -1
 
#     return C

# def knows(a,b):
#     return matrix[a][b]


# if __name__ == "__main__":
#     matrix = [  [ 0, 0, 1, 0 ],
#                 [ 0, 0, 1, 0 ],
#                 [ 0, 0, 0, 0 ],
#                 [ 0, 0, 1, 0 ] ]
#     n = 4
#     print(findCelebrity(matrix,n))

#Other Approach
 
def findCelebrity(matrix,n):
     
    # The graph needs not be constructed
    # as the edges can be found by
    # using knows function
       
    # degree array;
    indegree = [0 for x in range(n)]
    outdegree = [0 for x in range(n)]
       
    # Query for all edges
    for i in range(n):
        for j in range(n):
            x = (matrix[i][j]) # 0 0 1 0 0 0 1 0 0 0 0 0 0 1 0
            outdegree[i] += x
            indegree[j] += x
            
    # Find a person with indegree n-1
    # and out degree 0
    for i in range(n):
        if (indegree[i] == n - 1 and
           outdegree[i] == 0):
            return i
             
    return -1

if __name__ == "__main__":
    matrix = [  [ 0, 0, 1, 0 ],
                [ 0, 0, 1, 0 ],
                [ 0, 0, 0, 0 ],
                [ 0, 0, 1, 0 ] ]
    n = 4
    print(findCelebrity(matrix,n))
     