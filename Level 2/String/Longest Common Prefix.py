def commonPrefixUtil(str1,str2):
	res = ''
	i = 0
	j = 0
	while i<len(str1) and j<len(str2):
		if str1[i]!=str2[j]:
			break 
		res+=str1[i]
		i+=1
		j+=1
	return res

def commonPrefix(arr):
	n = len(arr)
	prefix = arr[0]
	for i in range(1,n):
		prefix = commonPrefixUtil(prefix,arr[i])
	return prefix

arr = ["apple","app","april"]
lcp = commonPrefix(arr)
print(lcp)