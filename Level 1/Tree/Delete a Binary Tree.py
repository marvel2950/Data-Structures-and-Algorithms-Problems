class Node:
    def __init__(self,data):
        self.val = data
        self.right = None
        self.left = None

def delete(root):
    if root==None:
        return
    delete(root.left)
    delete(root.right)
    del root


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
delete(root)
root = None