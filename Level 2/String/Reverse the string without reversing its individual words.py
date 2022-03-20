def reverseString(str):
    str = str.split(" ")
    str.reverse()
    str = ' '.join(str)
    return str

def spaceIndex(str,start):
    ind = -1
    for i in range(start,len(str)):
        if str[i] == " ":
            ind = i
            break 
    return ind

def reverseWord(str,start,end):
    while start < end:
        str[start],str[end] = str[end],str[start]
        start+=1
        end-=1

def reverseString(str):
    str = list(str)
    start = 0 
    while True:
        end = spaceIndex(str,start)
        if end!=-1:
            reverseWord(str,start,end-1)
            start = end+1 
        else:
            reverseWord(str,start,len(str)-1)
            break
    reverseWord(str,0,len(str)-1)
    str = ''.join(str)
    return str

str = "i like this program very much"
str = reverseString(str)
print(str)