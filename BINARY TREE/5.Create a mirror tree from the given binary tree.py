"""
Create a mirror tree from the given binary tree

Given a binary tree, the task is to create a new binary tree which is a mirror image of the given binary tree.

Examples: 

Input:
        5
       / \
      3   6
     / \
    2   4
Output:
Inorder of original tree: 2 3 4 5 6 
Inorder of mirror tree: 6 5 4 3 2
Mirror tree will be:
  5
 / \
6   3
   / \
  4   2

Input:
        2
       / \
      1   8
     /     \
    12      9
Output:
Inorder of original tree: 12 1 2 8 9 
Inorder of mirror tree: 9 8 2 1 12

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

def inorder(root):
    if not root:
        return 
    if root:
        inorder(root.getLeft())
        print(root.getData(),end=" ")
        inorder(root.getRight())
    return 


def convertToMirror(root):
    if not root:
        return 

    if root:
        convertToMirror(root.getRight())
        print(root.getData(), end=" ")
        convertToMirror(root.getLeft())
    return
        

        
if __name__ == "__main__":
    ''' Construct the following tree
        5
       / \
      3   6
     / \
    2   4
    '''
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    
    
    print("Inorder Traversal: ")
    inorder(root)

    print("\nMirror of Inorder Traversal: ")
    convertToMirror(root)
    

