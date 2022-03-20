def romanToDecimal(rom):
	value = {
		'M':1000,
		'D':500,
		'C':100,
		'L':50,
		'X':10,
		'V':5,
		'I':1
	}

	prev = 0
	dec = 0
	for i in range(len(rom)-1,-1,-1):
		if value[rom[i]]>=prev:
			dec+=value[rom[i]]
		else:
			dec-=value[rom[i]]
		prev = value[rom[i]]
	return dec
	
roman = 'MCMIV'
decimal = romanToDecimal(roman)
print(decimal)