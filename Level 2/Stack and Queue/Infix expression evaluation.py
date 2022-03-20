def applyOperator(beta,operator,alpha):
    alpha = int(alpha)
    beta = int(beta)
    if operator == "+": return alpha+beta
    elif operator == "-": return beta-alpha
    elif operator == "*": return alpha*beta
    elif operator == "/": return alpha/beta
    elif operator == "^": return alpha**beta

def evaluateInfix(infixExp):
    valueStack = []
    operatorStack = []
    precedence = {
        '+':1,
        '-':1,
        '*':2,
        '/':2,
        '^':3,
        '(':0,
        ')':4
    }
    i = 0
    while i<len(infixExp):
        if infixExp[i]=="(":
            operatorStack.append(infixExp[i])
        elif infixExp[i].isdigit():
            val = ''
            while i<len(infixExp) and infixExp[i].isdigit():
                val = val+infixExp[i]
                i+=1
            valueStack.append(val)
            i-=1
        elif infixExp[i]==")":
            while len(operatorStack)!=0 and operatorStack[-1] != "(":
                val2 = valueStack.pop()
                val1 = valueStack.pop()
                operator = operatorStack.pop()
                valueStack.append(applyOperator(val1,operator,val2))
            operatorStack.pop()
        else:
            while len(operatorStack)!=0 and precedence[operatorStack[-1]] >= precedence[infixExp[i]]:
                val2 = valueStack.pop()
                val1 = valueStack.pop()
                operator = operatorStack.pop()
                valueStack.append(applyOperator(val1,operator,val2))
            operatorStack.append(infixExp[i])
        i+=1
    while len(operatorStack)!=0:
        val2 = valueStack.pop()
        val1 = valueStack.pop()
        operator = operatorStack.pop()
        valueStack.append(applyOperator(val1,operator,val2))
    return valueStack[0]

infixExp = "(3+2)*(6-4)"
# infixVal = eval(infixExp)
# print(infixVal)
infixVal = evaluateInfix(infixExp)
print(infixVal)