"""
Preorder Tree Traversal – Iterative and Recursive
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
output: 1 2 4 3 5 7 8 6

"""
# Recursive method 
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


def Preorder_Traversal(Tree):
    if not Tree:
        return

    if Tree:
        print(Tree.getData(),end=" ")
        Preorder_Traversal(Tree.getLeft())
        Preorder_Traversal(Tree.getRight())
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
    print("Preorder Traversal: ")
    Preorder_Traversal(root)


# # Iterative Method

# from collections import deque
 
 
# # Data structure to store a binary tree node
# class Node:
#     def __init__(self, data=None, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right
 
 
# # Iterative function to perform preorder traversal on the tree
# def preorderIterative(root):
 
#     # return if the tree is empty
#     if root is None:
#         return
 
#     # create an empty stack and push the root node
#     stack = deque()
#     stack.append(root)
 
#     # loop till stack is empty
#     while stack:
 
#         # pop a node from the stack and print it
#         curr = stack.pop()
 
#         print(curr.data, end=' ')
 
#         # push the right child of the popped node into the stack
#         if curr.right:
#             stack.append(curr.right)
 
#         # push the left child of the popped node into the stack
#         if curr.left:
#             stack.append(curr.left)
 
#     # the right child must be pushed first so that the left child
#     # is processed first (LIFO order)
 
 
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
 
#     preorderIterative(root)