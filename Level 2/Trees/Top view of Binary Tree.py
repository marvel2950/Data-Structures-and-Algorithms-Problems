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

def topView(root):
    q = [root]
    hash = {}
    hash[0] = root.val
    root.val = [root.val,0]
    traversal = []

    while q!=[]:
        p = q.pop(0)
        if p:
            if p.left:
                q.append(p.left)
                depth = p.val[1]-1
                if depth not in hash:
                    hash[depth] = p.left.val
                p.left.val = [p.left.val,depth]
            if p.right:
                q.append(p.right)
                depth = p.val[1]+1
                if depth not in hash:
                    hash[depth] = p.right.val
                p.right.val = [p.right.val,depth]

    hash = sorted(hash.items(),key=lambda x:x[0])
    top = []
    for i in hash:
        top.append(i[1])
    return top
    #return list(hash.values())

# def topView(root):
#     traversal = verticalOrder(tree.root)
#     #print(traversal)
#     top = []
#     for row in traversal:
#         top.append(row[0])
#     return top
    
tree = BinarySearchTree()
nodes = [6,8,7,9,4,3,5]
for i in nodes:
    tree.insert(i)

top = topView(tree.root)
print(top)
