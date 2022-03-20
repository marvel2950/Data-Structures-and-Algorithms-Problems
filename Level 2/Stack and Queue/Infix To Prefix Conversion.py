def infixToPostfix(infixExp):
    postfixExp = []
    stack = []
    precedence = {
        '+':1,
        '-':1,
        '*':2,
        '/':2,
        '^':3,
        '(':0,
        ')':4
    }

    for i in infixExp:
        if i.isalpha():
            postfixExp.append(i)
        elif i=='(':
            stack.append(i)
        elif i==')':
            while len(stack)!=0 and stack[-1]!='(':
                a = stack.pop(-1)
                postfixExp.append(a)
            stack.pop(-1)
        else:
            while len(stack)!=0 and precedence[i]<precedence[stack[-1]]:
                postfixExp.append(stack.pop(-1))
            stack.append(i)
    
    while len(stack)!=0:
        postfixExp.append(stack.pop(-1))

    return ''.join(postfixExp)

def infixToPrefix(infixExp):
    infixExpUtil = []
    for i in infixExp:
        if i == "(":
            infixExpUtil.append(")")
        elif i == ")":
            infixExpUtil.append("(")
        else:
            infixExpUtil.append(i)
    infixExpUtil.reverse()
    postfixExp = infixToPostfix(infixExpUtil)
    prefixExp = postfixExp[::-1]
    return prefixExp

infixExp = "(a+b)*(c-d)"
prefixExp = infixToPrefix(infixExp)
print(prefixExp)