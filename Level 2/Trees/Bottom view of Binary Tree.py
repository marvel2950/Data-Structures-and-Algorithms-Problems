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

def bottomView(root):
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
                hash[depth] = p.left.val
                p.left.val = [p.left.val,depth]
            if p.right:
                q.append(p.right)
                depth = p.val[1]+1
                hash[depth] = p.right.val
                p.right.val = [p.right.val,depth]
    
    hash = sorted(hash.items(),key=lambda x:x[0])
    bottom = []
    for i in hash:
        bottom.append(i[1])
    return bottom

    # return list(hash.values())

# def  bottomView(root):
#     traversal = verticalOrder(root)
#     bottom = []
#     for row in traversal:
#         bottom.append(row[-1])
#     return bottom
    
tree = BinarySearchTree()
nodes = [6,8,7,9,4,3,5]
for i in nodes:
    tree.insert(i)

traversal = bottomView(tree.root)
print(traversal)
# for row in traversal:
#     print(*row)