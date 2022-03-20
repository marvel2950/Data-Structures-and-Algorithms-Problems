import sys

# def min(arr):
#     if len(arr)==0:
#         minEle = -1 
#     else:
#         arr.sort()
#         minEle = arr[0]
#     return minEle

# def max(arr):
#     if len(arr)==0:
#         maxEle = -1 
#     else:
#         arr.sort(reverse=True)
#         maxEle = arr[0]
#     return maxEle

# def min(arr):
#     if len(arr)==0:
#         minEle = -1 
#     else:
#         minEle = sys.maxsize
#         for i in arr:
#             if i<minEle:
#                 minEle = i
#     return minEle

# def max(arr):
#     if len(arr)==0:
#         maxEle = -1 
#     else:
#         maxEle = -sys.maxsize
#         for i in arr:
#             if i>maxEle:
#                 maxEle = i
#     return maxEle

arr = [9,6,1,2,5,4,8]
minEle = min(arr)
print(minEle)
maxEle = max(arr)
print(maxEle)