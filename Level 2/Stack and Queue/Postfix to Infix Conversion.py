def postfixToInfix(postfixExp):
    stack = []
    i = 0
    while i<len(postfixExp):
        if postfixExp[i].isalpha():
            stack.append(postfixExp[i])
        else:
            alpha = stack.pop(-1)
            beta = stack.pop(-1)
            strUtil = "(" + beta + postfixExp[i] + alpha + ")"
            stack.append(strUtil)
        print("Stack",i,stack)
        i+=1 
    return stack[0]

postfixExp = "ab+cd-*"
infixExp = postfixToInfix(postfixExp)
print(infixExp)