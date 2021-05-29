"""
Right View of Binary Tree 
Given a Binary Tree, find Right view of it. Right view of a Binary Tree is set of nodes visible when tree is viewed from right side.

Right view of following tree is 1 3 7 8.

          1
       /     \
     2        3
   /   \      /    \
  4     5   6    7
    \
     8

Example 1:

Input:
       1
    /    \
   3      2
Output: 1 2

Example 2:

Input:
     10
    /   \
  20     30
 /   \
40  60 
Output: 10 30 60
"""
from collections import deque
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    
def RightView(root):
    if not root:
        return

    queue = deque()
    queue.append(root)
    while queue:
        i = 0
        while i<len(queue):
            curr = queue.pop()
            i += 1
            if curr.right:
                queue.append(curr.right)
            if curr.left:
                queue.append(curr.left)
            if i == 1:
                print(curr.data, end=" ")

    

if __name__ == "__main__":
    """
          1
       /     \
     2        3
   /   \      / \
  4     5   6    7
    \
     8
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.right = TreeNode(8)
    print("Right View: ")
    RightView(root)