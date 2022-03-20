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


def preorder(root):
    traversal = []
    cur = root 
    stack = []
    while 1:
        while cur:
            traversal.append(cur.val)
            stack.append(cur)
            cur = cur.left
        if len(stack)==0:
            break
        cur = stack.pop(-1)
        cur = cur.right
    return traversal


tree = BinarySearchTree()
nodes = [6,8,7,9,4,3,5]
for i in nodes:
    tree.insert(i)
traversal = preorder(tree.root)
print(*traversal)