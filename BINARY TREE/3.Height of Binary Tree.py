"""
Height of Binary Tree

Given a binary tree, find its height.


Example 1:

Input:
     1
    /  \
   2    3
Output: 2

Example 2:

Input:
  2
   \
    1
   /
 3
Output: 3   

"""
#Iterrative Method 
from collections import deque
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class Soluation:
    def Height_of_Binary_Tree(self,root):
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        height = 0
        
        while queue:
            size = len(queue)
            while size >0:
                front = queue.popleft()

                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)

                size = size-1
            height += 1

        return height

if __name__ == "__main__":
    obj = Soluation()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    ans = obj.Height_of_Binary_Tree(root)
    print(ans)




# # Recursive Method 
# class TreeNode:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None

# def Height_of_Binary_Tree(root):
#     if not root:
#         return 0

#     return 1+ max(Height_of_Binary_Tree(root.left),Height_of_Binary_Tree(root.right))

# if __name__ == "__main__":
   
#     root = TreeNode(1)
#     root.left = TreeNode(2)
#     root.right = TreeNode(3)
#     ans = Height_of_Binary_Tree(root)
#     print(ans)
