class Node:
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None 

class BinarySearchTree:
    def __init__(self):
        self.root = None 

    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
        else:
            cur = self.root
            while 1:
                if data<cur.val:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = Node(data)
                        break
                elif data>cur.val:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = Node(data)
                        break 
                else:
                    break


def inorder(root):
    traversal = []
    cur = root
    stack = []
    while 1:
        while cur:
            stack.append(cur)
            cur=cur.left
        if len(stack)==0:
             break 
        cur = stack.pop(-1)
        traversal.append(cur.val)
        cur = cur.right
    return traversal

def inorderReversed(root):
    traversal = []
    cur = root
    stack = []
    while 1:
        while cur:
            stack.append(cur)
            cur=cur.right
        if len(stack)==0:
             break 
        cur = stack.pop(-1)
        traversal.append(cur.val)
        cur = cur.left
    return traversal


tree = BinarySearchTree()
nodes = [6,8,7,9,4,3,5]
for i in nodes:
    tree.insert(i)

traversal = inorder(tree.root)
print(*traversal)