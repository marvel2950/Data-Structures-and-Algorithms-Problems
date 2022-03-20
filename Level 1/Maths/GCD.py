import math
def primeFactos(n):
	factors = []
	while n%2==0:
		factors.append(2)
		n = n//2 
	for i in range(3,int(math.sqrt(n)+1),2):
		while n%i==0:
			factors.append(i)
			n = n//i 
	if n>2:
		factors.append(n)
	return factors

def gcd1(a,b):
	f1 = primeFactos(a)
	f2 = primeFactos(b)
	f1_count = {}
	f2_count = {}
	for i in f1:
		if i in f1_count:
			f1_count[i]=f1_count[i]+1 
		else:
			f1_count[i] = 1 
	for i in f2:
		if i in f2_count:
			f2_count[i]=f2_count[i]+1 
		else:
			f2_count[i] = 1 

	gcd_val = 1
	for i in list(set(f1+f2)):
		if i in f1_count and i in f2_count:
			gcd_val = gcd_val*i*min(f1_count[i],f2_count[i])
	return gcd_val

def gcd2(a,b):
	if a==0:
		return b 
	if b==0:
		return a 
	if a==b:
		return a
	if a>b:
		return gcd2(a-b,b)
	return gcd2(a,b-a)

def gcd3(a,b):
	if b==0:
		return a 
	return gcd3(b,a%b)

a = 20
b = 28 

gcd_val = gcd1(a,b)
print(gcd_val)

gcd_val = gcd2(a,b)
print(gcd_val)

gcd_val = gcd3(a,b)
print(gcd_val)

