"""
Inorder Tree Traversal – Iterative and Recursive


    Construct the following tree
               1
             /   \
            /     \
           2       3
          /      /   \
         /      /     \
        4      5       6
              / \
             /   \
            7     8
output = 4 2 1 7 5 8 3 6 
    
"""
#Recursive method 
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


def Inorder_traversal(Tree):
    if not Tree:
        return
    if Tree:
        Inorder_traversal(Tree.getLeft())
        print(Tree.getData(), end=" ")
        Inorder_traversal(Tree.getRight())
    return 

if __name__ == "__main__":
    """
    Construct the following tree
               1
             /   \
            /     \
           2       3
          /      /   \
         /      /     \
        4      5       6
              / \
             /   \
            7     8
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)

    Inorder_traversal(root)
