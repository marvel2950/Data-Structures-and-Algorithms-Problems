def trailingZeroes1(n):
	fact = 1
	for i in range(1,n+1):
		fact = fact*i 
	print(fact)
	count = 0
	while 1:
		rem = fact%10
		if rem!=0:
			break 
		fact = fact//10 
		count=count+1
	return count

n = 5
zeroes = trailingZeroes1(n)
print(zeroes)

def trailingZeroes2(n):
	count2 = 0
	count5 = 0
	for i in range(1,n+1):
		f = i
		while i%2==0:
			count2+=1 
			i = i//2
		while f%5==0:
			count5+=1 
			f = f//5
	return min(count2,count5)

n = 100
zeroes = trailingZeroes2(n)
print(zeroes)

def trailingZeroes3(n):
	if n<0:
		return -1
	count = 0
	while n>=5:
		n//=5
		count+=n
	return count

n = 100
zeroes = trailingZeroes3(n)
print(zeroes)

