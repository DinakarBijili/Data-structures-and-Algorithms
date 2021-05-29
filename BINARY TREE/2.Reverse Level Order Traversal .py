"""
Reverse Level Order Traversal
Given a binary tree of size N, find its reverse level order traversal. ie- the traversal must begin from the last level.

Example 1:

Input :
        1
      /   \
     3     2

Output: 3 2 1
Explanation:
Traversing level 1 : 3 2
Traversing level 0 : 1


Example 2:

Input :
       10
      /  \
     20   30
    / \ 
   40  60

Output: 40 60 20 30 10
Explanation:
Traversing level 2 : 40 60
Traversing level 1 : 20 30
Traversing level 0 : 10

"""
#post order
class TreeNode:
    def __init__(self, data , left = None, right = None):
        self.data = data
        self.left = left 
        self.right = right

    def getData(self):
        return self.data
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right

    
def reverse_traversal(root):
        if not root:
            return []

        if root:
            reverse_traversal(root.getLeft())
            reverse_traversal(root.getRight())
            print(root.data , end=" ")
        return 
            
            


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    reverse_traversal(root) 
    