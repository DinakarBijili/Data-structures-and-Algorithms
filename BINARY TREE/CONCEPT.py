# """
# The root of the tree is the node with no parents. There can be at most one root node in a tree.
# The edge refers to the link from parent to child.
# A node with NO children is called leaf node.
# Children of same parent are called siblings.


# """
class Node(object):
    def __init__(self, data = None):
        self.left = None
        self.right = None
        self.data = data
    
    # for setting left node
    def setLeft(self, node):
        self.left = node
    
    # for setting right node
    def setRight(self, node):
        self.right = node
        
    # for getting the left node
    def getLeft(self):
        return self.left
    
    # for getting right node
    def getRight(self):
        return self.right
    
    # for setting data of a node
    def setData(self, data):
        self.data = data
        
    # for getting data of a node
    def getData(self):
        return self.data
    
root = Node(1)
root.setLeft(Node(2))
root.setRight(Node(3))
root.left.setLeft(Node(4))
root.left.setRight(Node(5))
root.right.setLeft(Node(6))
root.right.setRight(Node(7))


''' Construct the following tree
              1
            /   \
           /     \
          2       3
         / \     / \
        4   5   6   7
'''


#Tree Travesal
# Inorder (left, data, right)
# Preorder (data, left, right)
# Postorder (left, right, data)

# Implementing tree traversals

# in this we traverse first to the leftmost node, then print its data and then traverse for rightmost node
def inorder(Tree):
    if Tree:
        inorder(Tree.getLeft())
        print(Tree.getData(), end = ' ')
        inorder(Tree.getRight())
    return

def mirror(Tree):
    if Tree:
        mirror(Tree.getRight())
        print(Tree.getData(),end=" ")
        mirror(Tree.getLeft())

# in this we first print the root node and then traverse towards leftmost node and then to the rightmost node
def preorder(Tree):
    if Tree:
        print(Tree.getData(), end = ' ')
        preorder(Tree.getLeft())
        preorder(Tree.getRight())
    return 
        

# in this we first traverse to the leftmost node and then to the rightmost node and then print the data
def postorder(Tree):
    if Tree:
        postorder(Tree.getLeft())
        postorder(Tree.getRight())
        print(Tree.getData(), end = ' ')
    return

print('Inorder  Traversal:')
inorder(root)
print('\nMirror of Inorder Traversal')
mirror(root)
print('\nPreorder Traversal:')
preorder(root)
print('\nPostorder Traversal:')
postorder(root)


''' Construct the following tree
              1
            /   \
           /     \
          2       3
         / \     / \
        4   5   6   7
'''
# OUTPUT:-
# Inorder  Traversal:
# 4 2 5 1 6 3 7 

# Mirror of Inorder Traversal 
# 7 3 6 1 5 2 4 
# Preorder Traversal:
# 1 2 4 5 3 6 7
# Postorder Traversal:
# 4 5 2 6 7 3 1



    
        
        
