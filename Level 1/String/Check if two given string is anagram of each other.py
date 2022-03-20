def isAnagram1(str1,str2):
    str1 = list(str1)
    str2 = list(str2)
    #print(str1,str2)
    str1.sort()
    str2.sort()
    #print(str1,str2)
    if str1==str2:
        return True 
    return False

str1 = 'ababca'
str2 = 'acbaba'
flag = isAnagram1(str1,str2)
print(flag)

def isAnagram2(str1,str2):
    count1 = {}
    count2 = {}
    for i in str1:
        if i in count1:
            count1[i]=count1[i]+1 
        else:
            count1[i]=1
    for i in str2:
        if i in count2:
            count2[i]=count2[i]+1 
        else:
            count2[i]=1

    for i in list(set(str1+str2)):
        if i not in count1 or i not in count2 or count1[i]!=count2[i]:
            return False 

    return True


str1 = 'ababca'
str2 = 'acbaba'
flag = isAnagram2(str1,str2)
print(flag)


def isAnagram3(str1,str2):
    count1 = {}
    for i in str1:
        if i in count1:
            count1[i]=count1[i]+1 
        else:
            count1[i]=1
    for i in str2:
        if i in count1:
            count1[i]=count1[i]-1 
        else:
            count1[i]=1

    for i,j in count1.items():
        if j!=0:
            return False 
    return True


str1 = 'ababca'
str2 = 'acbaa'
flag = isAnagram3(str1,str2)
print(flag)