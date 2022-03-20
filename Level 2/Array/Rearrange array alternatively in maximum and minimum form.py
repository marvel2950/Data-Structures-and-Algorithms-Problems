def rearrange(arr):
	n = len(arr)
	temp = n*[None]
	small = 0
	large = n-1
	flag = True 
	for i in range(n):
		if flag:
			temp[i] = arr[large]
			large-=1 
		else:
			temp[i] = arr[small]
			small+=1
		flag = 1-flag
	for i in range(n):
		arr[i] = temp[i]

def rearrange(arr):
	n = len(arr)
	maxIdx = n-1 
	minIdx = 0
	maxEle = arr[n-1]+1
	for i in range(n):
		if i%2==0:
			arr[i]+=(arr[maxIdx]%maxEle)*maxEle
			maxIdx-=1
		else:
			arr[i]+=(arr[minIdx]%maxEle)*maxEle
			minIdx+=1
	for i in range(n):
		arr[i] = arr[i]//maxEle

arr = [1,2,3,4,5,6]
rearrange(arr)
print(arr)