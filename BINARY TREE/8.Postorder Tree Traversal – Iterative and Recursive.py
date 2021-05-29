"""
Postorder Tree Traversal – Iterative and Recursive

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

output:4 2 7 8 5 6 3 1
    
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

def Postorder_Traversal(Tree):
    if not Tree:
        return

    if Tree:
        Postorder_Traversal(Tree.getLeft())
        Postorder_Traversal(Tree.getRight())
        print(Tree.getData(),end=" ")
    return 

if __name__ == "__main__":
    """
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
    print("Postorder Traversal: ")
    Postorder_Traversal(root)


# #Iterative method
# from collections import deque
# # Data structure to store a binary tree node
# class Node:
#     def __init__(self, data=None, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right
 
 
# # Iterative function to perform postorder traversal on the tree
# def postorderIterative(root):
 
#     # create an empty stack and push the root node
#     stack = deque()
#     stack.append(root)
 
#     # create another stack to store postorder traversal
#     out = deque()
 
#     # loop till stack is empty
#     while stack:
 
#         # pop a node from the stack and push the data into the output stack
#         curr = stack.pop()
#         out.append(curr.data)
 
#         # push the left and right child of the popped node into the stack
#         if curr.left:
#             stack.append(curr.left)
 
#         if curr.right:
#             stack.append(curr.right)
 
#     # print postorder traversal
#     while out:
#         print(out.pop(), end=' ')
 
 
# if __name__ == '__main__':
 
#     """ Construct the following tree
#                1
#              /   \
#             /     \
#            2       3
#           /      /   \
#          /      /     \
#         4      5       6
#               / \
#              /   \
#             7     8
#     """
 
#     root = Node(1)
#     root.left = Node(2)
#     root.right = Node(3)
#     root.left.left = Node(4)
#     root.right.left = Node(5)
#     root.right.right = Node(6)
#     root.right.left.left = Node(7)
#     root.right.left.right = Node(8)
 
#     postorderIterative(root)