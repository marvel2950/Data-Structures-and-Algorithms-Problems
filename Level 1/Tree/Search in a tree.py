# class Node:
#     def __init__(self,data):
#         self.right = None
#         self.left = None
#         self.val = data

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.left.right.left = Node(8)


# def rightView(root):
#     q = [root,None]
#     row = []
#     trav = []
#     prev = None
#     while len(q)!=0:
#         p = q.pop(0)
#         if p:
#             row.append(p.val)
#             if p.left:
#                 q.append(p.left)
#             if p.right:
#                 q.append(p.right)
#         else:
#             if len(row):trav.append(row[-1])
#             row = []
#             q.append(None)
#         if p==None and prev == None:
#             break 
#         prev = p 
#     return trav

# trav = rightView(root)
# print(*trav)
        

5/0
# except:
#     print("Some exception")

print("below")