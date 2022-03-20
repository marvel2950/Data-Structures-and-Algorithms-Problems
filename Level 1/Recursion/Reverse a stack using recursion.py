op_stack = []
def reverseAStack(ip_stack):
    if len(ip_stack)==1:
        op_stack.append(ip_stack[0])
        return
    alpha = ip_stack.pop(-1)
    op_stack.append(alpha)
    reverseAStack(ip_stack)

ip_stack = [1,2,3]
reverseAStack(ip_stack)
print(op_stack)
