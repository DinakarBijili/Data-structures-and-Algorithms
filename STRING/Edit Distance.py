"""
Edit Distance 

Given two strings s and t. Find the minimum number of operations that need to be performed on str1 to convert it to str2. The possible operations are:

Insert
Remove
Replace
 

Example 1:

Input: 
s = "geek", t = "gesek"
Output: 1
Explanation: One operation is required 
inserting 's' between two 'e's of str1.
Example 2:

Input : 
s = "gfg", t = "gfg"
Output: 
0
Explanation: Both strings are same.

"""
# def Edit_distance(s, t):
#     count = 0
#     if s == t:
#         return 0
#     if s not in t:
#         count += 1
#     return count

# if __name__ == "__main__":
#     s = "ecfbefdcfca"
#     t = "badfcbebbf"
#     print(Edit_distance(s, t)) # output 9 



def edit_distance(s1, s2):
    m=len(s1)+1
    n=len(s2)+1

    tbl = {}
    for i in range(m): 
        tbl[i,0]=i 
        
    for j in range(n): 
        tbl[0,j]=j
        print(tbl)
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)

    return tbl[i,j]
if __name__ == "__main__":
    s = "geek"
    t = "gesek"
    print(edit_distance(s, t)) # output 9 