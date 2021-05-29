"""
Left View of Binary Tree
Given a Binary Tree, print Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side. The task is to complete the function leftView(), which accepts root of the tree as argument.

Left view of following tree is 1 2 4 8.

          1
       /     \
     2        3
   /     \    /    \
  4     5   6    7
   \
     8   
output : 1 2 4 8

Example 2: 

Input:
   1
 /  \
3    2
Output: 1 3

"""
#Iterative method 
from collections import deque
class Treenode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def Left_view(Tree):
    if not Tree:
        return
    queue = deque()
    queue.append(Tree)
    while queue:
        i = 0
        while i < len(queue):
            # pointer to store the current node
            curr = queue.popleft()
            i += 1

            if i == 1:
                print(curr.data, end=" ")
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

if __name__ == "__main__":
    """
          1
       /     \
     2        3
   /   \     / \
  4     5   6    7
   \
     8   
    """
    root = Treenode(1)
    root.left = Treenode(2)
    root.right = Treenode(3)
    root.left.left = Treenode(4)
    root.left.right = Treenode(5)
    root.right.left = Treenode(6)
    root.right.right = Treenode(7)
    root.left.left.right = Treenode(8)
    print("Left View: ")
    Left_view(root)
    