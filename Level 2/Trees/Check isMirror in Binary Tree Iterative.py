import copy
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

def levelOrder(root):
    traversal = []    
    row = []
    q = [root,None]
    prev = None
    while len(q)!=0:
        p = q.pop(0)
        if p:
            row.append(p.val)
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)
        else:
            q.append(None)
            if row!=[]:
                traversal.append(row)
            row = []
        if p==None and prev==None:
            break 
        prev = p
    return traversal


def mirror(root):
    q = [root]
    while len(q)!=0:
        p = q.pop(0)
        if p:
            p.left,p.right = p.right, p.left
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)
    return root

def isMirror(r1,r2):
    st1 = []
    st2 = []
    while 1:
        while r1 and r2:
            if r1.val != r2.val:
                return False 
            st1.append(r1)
            st2.append(r2)
            r1 = r1.left
            r2 = r2.right

        if (r1==None and r2!=None) or (r2==None and r1!=None):
            return False

        if len(st1)!=0 and len(st2)!=0:
            r1 = st1.pop(-1)
            r2 = st2.pop(-1)
            r1 = r1.right
            r2 = r2.left
        else:
            break 
    return True

tree = BinarySearchTree()
nodes = [6,8,7,9,4,3,5]
for i in nodes:
    tree.insert(i)

traversal = levelOrder(tree.root)
for row in traversal:
    print(*row)


root = copy.deepcopy(tree.root)
rootMirror = mirror(root)
rootMirror.val = 98

traversal = levelOrder(rootMirror)
for row in traversal:
    print(*row)

flag = isMirror(tree.root,rootMirror)
print(flag)