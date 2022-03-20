def fact(n):
    res = 1 
    for i in range(2,n+1):
        res=res*i 
    return res

def nCr(n,r):
    return fact(n)//(fact(r)*fact(n-r))


def printPascal(n):
	for i in range(0,n):
		for k in range(1,n-i):
			print(" ",end="")
		for j in range(0,i+1):
			print(nCr(i,j),end=" ")
		print()

n = 7
printPascal(n)

def printPascal(n):
	arr = [[0 for x in range(n)]
			for y in range(n)]
	for line in range(0,n):
		for k in range(1,n-line):
			print(" ",end="")
		for i in range(0,line+1):
			if i==0 or i==line:
				arr[line][i] = 1
				print(arr[line][i],end=" ")
			else:
				arr[line][i] = arr[line-1][i-1]+arr[line-1][i]
				print(arr[line][i],end=" ")
		print()
			
n = 7
printPascal(n)


def printPascal(n):
	arr1 = [0 for x in range(n)] # => Previous line
	arr2 = [0 for x in range(n)] # => Present line
	for line in range(0,n):
		for k in range(1,n-line):
			print(" ",end="")
		for i in range(0,line+1):
			if i==0 or i==line:
				arr2[i] = 1
				print(arr2[i],end=" ")
			else:
				arr2[i] = arr1[i-1]+arr1[i]
				print(arr2[i],end=" ")

		arr1 = arr2[:]
		arr2 = [0 for x in range(n)]
		print()
			
n = 7
printPascal(n)


def printPascal(n):
	for i in range(1,n+1):
		for k in range(1,n-i):
			print(" ",end="")
		c = 1
		for j in range(1,i+1):
			print(c,end=" ")
			c = c*(i-j)//j
		print()

n = 7
printPascal(n)