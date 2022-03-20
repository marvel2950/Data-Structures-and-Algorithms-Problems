class Node:
    def __init__ (self,data):
        self.val = data 
        self.left = None
        self.right = None

def sum(root):
    if root==None:
        return 0 
    return root.val+sum(root.left)+sum(root.right)

def isSumTree(root):
    if root==None:
        return True 
    if root.left==None and root.right==None:
        return True 
    leftSum = sum(root.left)
    rightSum = sum(root.right)
    if root.val == leftSum+rightSum:
        if isSumTree(root.left) and isSumTree(root.right):
            return True 
    return False

def isLeaf(root):
    if root.left==None and root.right==None:
        return True 
    return False

def isSumTree(root):
    if root==None:
        return True 
    if isLeaf(root):
        return True 
    if isSumTree(root.left) and isSumTree(root.right):
        if root.left==None:
            leftSum = 0
        elif isLeaf(root.left):
            leftSum = root.left.val
        else:
            leftSum = 2*root.left.val

        if root.right==None:
            rightSum = 0
        elif isLeaf(root.right):
            rightSum = root.right.val
        else:
            rightSum = 2*root.right.val
            
        if root.val==leftSum+rightSum:
            return True 
        else:
            return False
    return False

tree = Node(48)
tree.left = Node(8)
tree.right = Node(16)     
tree.left.left = Node(3)
p = tree.left.right = Node(5)     
q = tree.right.left = Node(7)
tree.right.right = Node(9)     

# tree = Node(6)
# tree.left = Node(4)
# tree.right = Node(8)     
# tree.left.left = Node(3)
# p = tree.left.right = Node(5)     
# q = tree.right.left = Node(7)
# tree.right.right = Node(9)     

flag = isSumTree(tree)
print(flag)