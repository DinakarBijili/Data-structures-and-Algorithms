"""
ZigZag Tree Traversal 


Given a Binary Tree. Find the Zig-Zag Level Order Traversal of the Binary Tree.

 

Example 1:

Input:
        3
      /   \
     2     1
Output:
3 1 2
Example 2:

Input:
           7
        /     \
       9       7
     /  \     /   
    8    8   6     
   /  \
  10   9 
Output:
7 7 9 8 8 6 9 10 

"""
class TreeNode:
    def __init__(self,data ):
        self.data = data 
        self.left = None
        self.right = None
class Soluation:
    def zigzagLevelOrder(self, root):
        reverse = False
        result = []
        if not root:
            return []
        que = [root]
        while que:
            tmpq = []
            values = []
            for node in que:
                values.append(node.data)
                if node.left:
                    tmpq.append(node.left)
                    
                if node.right:
                    tmpq.append(node.right)
            que = tmpq
            if reverse:
                values.reverse()
            reverse = not reverse
            result.append(values)
        return result

if __name__ == "__main__":
    """
           7
        /     \
       9       7
     /  \     /   
    8    8   6     
   /  \
  10   9 

    """
    root = TreeNode(7)
    root.left = TreeNode(9)
    root.right = TreeNode(7)
    root.left.left = TreeNode(8)
    root.left.right = TreeNode(8)
    root.right.left = TreeNode(6)
    root.left.left.left = TreeNode(10)
    root.left.left.right = TreeNode(9)

    print("ZigZag: ")
    res =Soluation().zigzagLevelOrder(root)
    print(res)
