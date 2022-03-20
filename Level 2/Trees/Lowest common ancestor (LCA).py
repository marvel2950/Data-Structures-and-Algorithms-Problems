class Node:
    def __init__ (self,data):
        self.val = data 
        self.left = None
        self.right = None

def lca(root,p,q):
    if root==None:
        return None 
    if root==p or root == q:
        return root 
    left = lca(root.left,p,q)
    right = lca(root.right,p,q)

    if left!=None and right!=None:
        return root 
    else:
        return left if left else right

tree = Node(6)
tree.left = Node(4)
tree.right = Node(8)     
tree.left.left = Node(3)
p = tree.left.right = Node(5)     
q = tree.right.left = Node(7)
tree.right.right = Node(9)     

lcaNode = lca(tree,p,q)
print(lcaNode.val)