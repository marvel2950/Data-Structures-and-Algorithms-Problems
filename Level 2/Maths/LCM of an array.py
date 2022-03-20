def gcd(a,b):
	if b==0:
		return a 
	return gcd(b,a%b)

def lcm(a,b):
	return a*b//gcd(a,b)

def lcmArray(arr):
    if len(arr)<2:
        return -1
    num1 = arr[0]
    num2 = arr[1]
    lcmVal = lcm(num1,num2)
    for i in range(2,len(arr)):
        lcmVal = lcm(lcmVal,arr[i])
    return lcmVal

arr = [1, 2, 3, 4, 28]
lcmVal = lcmArray(arr)
print(lcmVal)