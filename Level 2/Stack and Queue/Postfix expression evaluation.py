def applyOperator(beta,operator,alpha):
    alpha = int(alpha)
    beta = int(beta)
    if operator == "+": return alpha+beta
    elif operator == "-": return beta-alpha
    elif operator == "*": return alpha*beta
    elif operator == "/": return alpha/beta
    elif operator == "^": return alpha**beta

def evaluatePostfix(postfixExp):
    stack = []
    i = 0
    while i <len(postfixExp):
        if postfixExp[i].isdigit():
            stack.append(postfixExp[i])
        else:
            alpha = stack.pop()
            beta = stack.pop()
            val = applyOperator(beta,postfixExp[i],alpha)
            stack.append(val)
        i+=1
        print(stack)
    return int(stack[0])

postfixExp = "3243+64-*"
postfixVal = evaluatePostfix(postfixExp)
print(postfixVal)

def applyOperator(beta,operator,alpha):
    alpha = int(alpha)
    beta = int(beta)
    if operator == "+": return alpha+beta
    elif operator == "-": return beta-alpha
    elif operator == "*": return alpha*beta
    elif operator == "/": return alpha/beta
    elif operator == "^": return alpha**beta

def evaluatePostfix(postfixExp):
    stack = []
    i = 0
    while i <len(postfixExp):
        if postfixExp[i].isdigit():
            val = ''
            while i<len(postfixExp) and postfixExp[i].isdigit():
                val = val+postfixExp[i]
                i+=1
            stack.append(val)
            i-=1
        elif postfixExp[i] == " ":
            pass
        else:
            alpha = stack.pop()
            beta = stack.pop()
            val = applyOperator(beta,postfixExp[i],alpha)
            stack.append(val)
        i+=1
        #print(stack)
    return int(stack[0])

postfixExp = "32 43 + 6 4 - *"
postfixVal = evaluatePostfix(postfixExp)
print(postfixVal)