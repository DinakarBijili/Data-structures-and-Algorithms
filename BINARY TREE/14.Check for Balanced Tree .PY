"""
Check for Balanced Tree 


Given a binary tree, find if it is height balanced or not. 
A tree is height balanced if difference between heights of left and right subtrees is not more than one for all nodes of tree. 

A height balanced tree
        1
     /     \
   10      39
  /
5

An unbalanced tree
        1
     /    
   10   
  /
5

Example 1:

Input:
      1
    /
   2
    \
     3 
Output: 0
Explanation: The max difference in height
of left subtree and right subtree is 2,
which is greater than 1. Hence unbalanced
Example 2:

Input:
       10
     /   \
    20   30 
  /   \
 40   60
Output: 1
Explanation: The max difference in height
of left subtree and right subtree is 1.
Hence balanced. 

"""
class TreeNode:
    def __init__(self,data ):
        self.data = data 
        self.left = None
        self.right = None

    def getData(self):
        return self.data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right



def Check_bal_Tree(node):
        if node is None:
            return 0
    
        l = Check_bal_Tree(node.left)
        r = Check_bal_Tree(node.right)

        if abs(l - r)<=1:
            return l and r



if __name__ == "__main__":
    """
       10
     /   \
    20   30 
  /   \
 40   60
    """
    root = TreeNode(10)
    root.left = TreeNode(20)
    root.right = TreeNode(30)
    root.left.left = TreeNode(40)
    root.left.right = TreeNode(60)
    res = Check_bal_Tree(root)
    print(res)