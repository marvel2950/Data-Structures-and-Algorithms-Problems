class Node:
    def __init__ (self,data):
        self.val = data 
        self.left = None
        self.right = None

def rootToLeaf(root,stack = []):
    if root==None:
        return
    stack.append(root.val)
    rootToLeaf(root.left)
    if root.left==None and root.right==None:
        print(*stack)
    rootToLeaf(root.right)
    stack.pop(-1)

tree = Node(6)
tree.left = Node(4)
tree.right = Node(8)     
tree.left.left = Node(3)
p = tree.left.right = Node(5)     
q = tree.right.left = Node(7)
tree.right.right = Node(9)     

rootToLeaf(tree)