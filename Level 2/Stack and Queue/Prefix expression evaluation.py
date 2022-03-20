def applyOperator(beta,operator,alpha):
    alpha = int(alpha)
    beta = int(beta)
    if operator == "+": return alpha+beta
    elif operator == "-": return beta-alpha
    elif operator == "*": return alpha*beta
    elif operator == "/": return alpha/beta
    elif operator == "^": return alpha**beta

def evaluatePrefix(prefixExp):
    stack = []
    i =  0
    prefixExp = prefixExp[::-1]
    while i<len(prefixExp):
        if prefixExp[i].isdigit():
            val = ''
            while i<len(prefixExp) and prefixExp[i].isdigit():
                val = val+prefixExp[i]
                i+=1
            stack.append(val)
            i-=1
        elif prefixExp[i] == " ":
            pass
        else:
            alpha = stack.pop()
            beta = stack.pop()
            val = applyOperator(alpha,prefixExp[i],beta)
            stack.append(val)
        i+=1
        #print(stack)
    return int(stack[0])

prefixExp = "* + 32 43 - 6 4"
prefixVal = evaluatePrefix(prefixExp)
print(prefixVal)