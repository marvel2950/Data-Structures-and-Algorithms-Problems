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

traversal = []
def inorder(root):
    if root==None:
        return
    if root.left:
        inorder(root.left)
    global traversal
    traversal.append(root.val)
    if root.right:
        inorder(root.right)

def search(root,key):
    if root==None or root.val==key:
        return root
    if root.val<key:
        return search(root.right,key)
    return search(root.left,key)

def inorderPred(root,node):
    pred = None 
    store = None
    if node.left!=None: 
        temp = node.left
        while temp.right!=None:
            temp = temp.right 
        pred = temp 
    else:
        cur = root 
        while cur.val!=node.val:
            if node.val>cur.val:
                store = cur
                cur = cur.right
            else:
                cur = cur.left 
        pred = store 
    return pred

tree = BinarySearchTree()
nodes = [6,8,7,9,4,3,5]
for i in nodes:
    tree.insert(i)
key = 3
node = search(tree.root,key)
pred = inorderPred(tree.root,node)
print(pred)


# key = 3
# inorder(tree.root)
# for i in range(0,len(traversal)):
#     if traversal[i]==key:
#         index = i 
#         break 
# if index-1>=0:
#     print(traversal[index-1])
# else:
#     print(-1)
