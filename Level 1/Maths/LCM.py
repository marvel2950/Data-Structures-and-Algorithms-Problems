import math

def gcd(a,b):
	if b==0:
		return a 
	return gcd(b,a%b)

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

def lcm1(a,b):
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

	lcm_val = 1
	for i in list(set(f1+f2)):
		if i in f1_count and i in f2_count:
			if f1_count[i]>f2_count[i]:
				alpha = f2_count[i]+(f1_count[i]-f2_count[i])
			else:
				alpha = f1_count[i]+(f2_count[i]-f1_count[i])
		elif i in f1_count:
			alpha = f1_count[i]
		else:
			alpha = f2_count[i]
		lcm_val = lcm_val*i*alpha
	return lcm_val

def lcm2(a,b):
	return a*b//gcd(a,b)

a = 15
b = 20

lcm_val = lcm1(a,b)
print(lcm_val)


lcm_val = lcm2(a,b)
print(lcm_val)
