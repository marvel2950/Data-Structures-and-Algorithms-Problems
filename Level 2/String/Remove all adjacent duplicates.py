def removeAdjacentDuplicates(str):
    str = list(str)
    flag = True
    while flag:
        i = 0
        check = False
        while i<len(str)-1:
            if str[i]==str[i+1]:
                str.pop(i)
                str.pop(i)
                check = True 
            else:
                i+=1 
        if check==False:
            flag = False 
    str = ''.join(str)
    return str

str = "azxxzy"
str = removeAdjacentDuplicates(str)
print(str)