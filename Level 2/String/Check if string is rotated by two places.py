def isRotated(str2,str1):
	if len(str1)!=len(str2):
		return False 
	if len(str1)<2:
		return str1 == str2 
	
	l = len(str2)
	anticlockStr = str2[l-2:]+str2[0:l-2]
	clockStr = str2[2:]+str2[0:2]

	return (str1==clockStr) or (str1==anticlockStr)

str1 = 'ineuron'
#Clockwise
# str2 = 'euronin'
#Anti-Clockwise
str2 = "onineur"
flag = isRotated(str2,str1)
print(flag)