class Node:
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None 

class Tree:
    def __init__(self):
        self.root = None 
    
tree = Tree()
print(tree.root)