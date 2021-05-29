"""
Top View of Binary Tree 

Given below is a binary tree. The task is to print the top view of binary tree. Top view of a binary tree is the set of nodes visible when the tree is viewed from the top. For the given below tree

       1
    /     \
   2       3
  /  \    /   \
4    5  6      7

Top view will be: 4 2 1 3 7
Note: Return nodes from leftmost node to rightmost node.

Example 1:

Input:
      1
   /    \
  2      3
Output: 2 1 3
Example 2:

Input:
       10
    /      \
  20        30
 /   \    /    \
40   60  90    100
Output: 40 20 10 30 100

"""
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def getData(self):
        return self.data    

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

def TopView(Tree):
    if not Tree:
        return []
    if Tree:
        TopView(Tree.getLeft())
        TopView(Tree.getRight)
        print(Tree.data)


if __name__ == "__main__":
    """
       1
    /     \
   2       3
  /  \    /   \
4    5  6      7

Top view will be: 4 2 1 3 7
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print("Top View: ")
    TopView(root)