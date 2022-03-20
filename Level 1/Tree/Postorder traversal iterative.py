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

def postOrder(root):
    traversal = []
    cur = root
    stack1= [cur]
    stack2 = []
    while len(stack1)!=0:
        cur = stack1.pop(-1)
        stack2.append(cur.val)
        if cur.left:
            stack1.append(cur.left)
        if cur.right:
            stack1.append(cur.right)
    
    while len(stack2)!=0:
        alpha = stack2.pop(-1)
        traversal.append(alpha)
    return traversal

tree = BinarySearchTree()
nodes = [6,8,7,9,4,3,5]
for i in nodes:
    tree.insert(i)
traversal = postOrder(tree.root)
print(*traversal)
