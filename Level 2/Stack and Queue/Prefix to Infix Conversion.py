def prefixToInfix(prefixExp):
    stack = []
    i = len(prefixExp)-1 
    while i>=0:
        if prefixExp[i].isalpha():
            stack.append(prefixExp[i])
        else:
            alpha = stack.pop(-1)
            beta = stack.pop(-1)
            strUtil = "(" + alpha + prefixExp[i] + beta + ")"
            stack.append(strUtil)
        i-=1
        print("Stack",stack)
    return stack[0]

prefixExp = "*+ab-cd"
infixExp = prefixToInfix(prefixExp)
print(infixExp)