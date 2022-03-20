import math
def egyptianFraction(num,den):
	denVals = []
	while num != 0:
		alpha = math.ceil(den/num)
		denVals.append(alpha)
		num = alpha*num - den
		den = den*alpha
	return denVals

def printFraction(num,den,denVals):
	print("{0}/{1} =".format(num,den),end=" ")
	for i in range(len(denVals)):
		if i!=len(denVals)-1:
			print("1/{0} +".format(denVals[i]),end=" ")
		else:
			print("1/{0}".format(denVals[i]),end=" ")

num = 6
den = 14
denVals = egyptianFraction(num,den)
printFraction(num,den,denVals)