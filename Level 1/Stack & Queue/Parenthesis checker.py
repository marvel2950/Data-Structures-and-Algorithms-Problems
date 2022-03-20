def areBracketsBalanced(exp):
    stack = []
    for char in exp:
        if char in ['(','[','{']:
            stack.append(char)
        elif char in [')',']','}']:
            if not stack:
                return False
            alpha = stack.pop()
            if alpha == "(":
                if char != ")":
                    return False
            if alpha == "[":
                if char != "]":
                    return False
            if alpha == "{":
                if char != "}":
                    return False
    if stack:
        return False
    return True

exp = "{[()][}"
flag = areBracketsBalanced(exp)
print(flag)