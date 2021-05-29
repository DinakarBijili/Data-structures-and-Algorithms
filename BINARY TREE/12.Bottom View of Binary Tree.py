"""
Bottom View of Binary Tree
Given a binary tree, print the bottom view from left to right.
A node is included in bottom view if it can be seen when we look at the tree from bottom.

                      20
                    /    \
                  8       22
                /   \        \
              5      3       25
                    /   \      
                  10    14

For the above tree, the bottom view is 5 10 3 14 25.
If there are multiple bottom-most nodes for a horizontal distance from root, then print the later one in level traversal. For example, in the below diagram, 3 and 4 are both the bottommost nodes at horizontal distance 0, we need to print 4.

                      20
                    /    \
                  8       22
                /   \     /   \
              5      3 4     25
                     /    \      
                 10       14

For the above tree the output should be 5 10 4 14 25.

Example 1:
Input:
       1
     /   \
    3     2
Output: 3 1 2
Explanation:
First case represents a tree with 3 nodes
and 2 edges where root is 1, left child of
1 is 3 and right child of 1 is 2.

Thus nodes of the binary tree will be
printed as such 3 1 2.

Example 2:
Input:
         10
       /    \
      20    30
     /  \
    40   60
Output: 40 20 60 30

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

def Bottom_view(root):
    if root:
        Bottom_view(root.getLeft())
        Bottom_view(root.getRight())
        print(root.getData(), end=" ")
    return 

if __name__ == "__main__":
    """
    Input:
         10
       /    \
      20    30
     /  \
    40   60
    """
    root = TreeNode(10)
    root.left = TreeNode(20)
    root.right = TreeNode(30)
    root.left.left = TreeNode(40)
    root.left.right = TreeNode(60)

    print("Bottom View: ")
    Bottom_view(root)