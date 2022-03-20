def nextAlphabeticalElement(string,key,start,end):
    res = -1
    while start <= end:
        mid = (start+end)//2 
        if key==string[mid]:
            start = mid+1
        elif key < string[mid]:
            res = string[mid]
            end = mid-1  
        elif key > string[mid]:
            start = mid+1
    return res

string = 'abchjoqt'
key = 'd'
start = 0
end = len(string)-1
nextAlpha = nextAlphabeticalElement(string,key,start,end)
print(nextAlpha)