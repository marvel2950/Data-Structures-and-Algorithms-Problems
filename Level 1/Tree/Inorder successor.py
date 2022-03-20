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

def inorderSuccessor(root,node):
    succ = None
    store = None
    if node.right!=None:
        temp = node.right
        while temp.left!=None:
            temp = temp.left 
        succ = temp 
    else:
        cur = root 
        while cur.val!=node.val:
            if node.val<=cur.val:
                store = cur 
                cur = cur.left 
            else:
                cur = cur.right 
        succ = store 
    return succ


tree = BinarySearchTree()
nodes = [6,8,7,9,4,3,5]
for i in nodes:
    tree.insert(i)
key = 9
node =search(tree.root,key)
succNode = inorderSuccessor(tree.root,node)
print(succNode)

# key = 9
# inorder(tree.root)
# for i in range(0,len(traversal)):
#     if key==traversal[i]:
#         index = i
#         break 
# if index+1<len(traversal):
#     print(traversal[index+1])
# else:
#     print(-1)