def maxDivide(num,d):
	while num%d == 0:
		num = num//d
	return num

def isUgly(num):
	num = maxDivide(num,2)
	num = maxDivide(num,3)
	num = maxDivide(num,5)

	if num == 1:
		return True 
	else:
		return False

def nthUglyNum(n):
	i = 1
	count = 1
	while n>count:
		i += 1
		if isUgly(i):
			count += 1
	return i

n = 10
num = nthUglyNum(n)
print(num)