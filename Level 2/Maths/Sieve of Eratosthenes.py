import math
def isPrime(n):
	if n<=1:
		return False 
	for i in range(2,int(math.sqrt(n))+1):
		if n%i==0:
			return False 
	return True

def primeRange(n):
	ans = []
	for i in range(1,n+1):
		if isPrime(i):
			ans.append(i)
	return ans

n = 20
primeNums = primeRange(n)
print(primeNums)


def sieveOfEratosthenes(n):
	prime = [True for i in range(n+1)]
	prime[0],prime[1] = False, False
	ans = []
	p = 2
	while p*p <=n:
		if prime[p] == True:
			for i in range(p*p,n+1,p):
				prime[i] = False

		p+=1

	for i in range(1,n+1):
		if prime[i]:
			ans.append(i)
	return ans

n = 20
primeNums = sieveOfEratosthenes(n)
print(primeNums)