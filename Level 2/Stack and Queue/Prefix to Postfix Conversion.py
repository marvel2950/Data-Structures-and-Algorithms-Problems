def prefixToPostfix(prefixExp):
    stack = []
    i = len(prefixExp)-1 
    while i>=0:
        if prefixExp[i].isalpha():
            stack.append(prefixExp[i])
        else:
            alpha = stack.pop(-1)
            beta = stack.pop(-1)
            strUtil =  alpha  + beta + prefixExp[i]
            stack.append(strUtil)
        i-=1
        print("Stack",stack)
    return stack[0]

prefixExp = "*+ab-cd"
postExp = prefixToPostfix(prefixExp)
print(postExp)