"""
Level order traversal

Given a binary tree, find its level order traversal.
Level order traversal of a tree is breadth-first traversal for the tree.


Example 1:

Input:
    1
  /   \ 
 3     2
Output:1 3 2
Example 2:

Input:
        10
     /      \
    20       30
  /   \
 40   60
Output:10 20 30 40 60 N N

"""
class TreeNone:
    def __init__(self, data, left=None, right = None):
        self.data = data
        self.left = left
        self.right = right


    def __str__(self):
        return str(self.data)

class Soluation:
    def Level_order_traversal(self,root):
            res = []
            if root is None:
                return None
            queue = []
            queue.append(root)
            while len(queue)>0:
                node = queue.pop(0)
                res.append(node.data)
                
                if node.left != None:
                    queue.append(node.left)

                if node.right != None:
                    queue.append(node.right)
            return res
                    

if __name__ == "__main__":
    obj = Soluation()
    # node = list(map(int, input().split()))
    root = TreeNone(10)
    root.left = TreeNone(20)
    root.right = TreeNone(30)
    root.left.left = TreeNone(40)
    root.left.right = TreeNone(50)
    ans = obj.Level_order_traversal(root)

    print(ans)