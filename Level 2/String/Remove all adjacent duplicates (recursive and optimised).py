def remove(str,lastRemoved):
    if len(str)==0 or len(str)==1:
        return str
    if str[0]==str[1]:
        lastRemoved = str[0]
        while len(str)>1 and str[0]==str[1]:
            str = str[1:]
        str = str[1:]
        return remove(str,lastRemoved)
    rem = remove(str[1:],lastRemoved)
    if len(rem)!=0 and rem[0]==str[0]:
        lastRemoved = str[0]
        return rem[1:]
    if len(rem)==0 and lastRemoved == str[0]:
        return rem
    return ([str[0]]+rem)

def removeAdjacentDuplicates(str):
    lastRemoved = 0
    return ''.join(remove(list(str),lastRemoved))

str = "azxxzy"
str = removeAdjacentDuplicates(str)
print(str)