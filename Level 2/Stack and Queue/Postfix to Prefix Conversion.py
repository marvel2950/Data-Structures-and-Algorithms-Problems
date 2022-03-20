def postfixToPrefix(postfixExp):
    stack = []
    i = 0
    while i<len(postfixExp):
        if postfixExp[i].isalpha():
            stack.append(postfixExp[i])
        else:
            alpha = stack.pop(-1)
            beta = stack.pop(-1)
            strUtil = postfixExp[i]+beta+alpha
            stack.append(strUtil)
        print("Stack",i+1,stack)
        i+=1
        
    return stack[0]

postfixExp = "ab+cd-*"
prefixExp = postfixToPrefix(postfixExp)
print(prefixExp)