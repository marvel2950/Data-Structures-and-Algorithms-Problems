def gcd(a,b):
	if b==0:
		return a 
	return gcd(b,a%b)

def gcdArray(arr):
    if len(arr)==0:
        return -1
    res = arr[0]
    for i in range(1,len(arr)):
        if arr[i]==1:
            res = 1 
            break
        res = gcd(res,arr[i])
    return res

arr = [2,4,6,8,16]
gcdVal = gcdArray(arr)
print(gcdVal)

