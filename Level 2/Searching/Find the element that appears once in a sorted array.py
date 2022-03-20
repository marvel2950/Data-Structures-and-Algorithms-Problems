def solve(arr):
	hash = {}
	n = len(arr)
	ans = -1
	for i in arr:
		if i in hash:
			hash[i]+=1 
		else:
			hash[i] = 1
	for ele,count in hash.items():
		if count==1:
			ans = ele 
			break 
	return ans

def solve(arr):
	ans = -1 
	n = len(arr)
	for i in range(0,n-1,2):
		if arr[i]!=arr[i+1]:
			ans = arr[i]
			break 
	if arr[n-2]!=arr[n-1]:
		ans = arr[n-1]
	return ans

def solve(arr):
	xor = 0
	n = len(arr)
	for i in arr:
		xor = xor^i 
	return xor

arr = [1,1,2,4,4,5,5,6,6]
ans = solve(arr)
print(ans)