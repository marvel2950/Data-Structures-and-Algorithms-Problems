value = {
		1:'I',
        4:'IV',
        5:'V',
        9:'IX',
        10:'X',
        40:'XL',
        50:'L',
        90:'XC',
        100:'C',
        400:'CD',
        500:'D',
        900:'CM',
        1000:'M'
	}

def decimalToRoman(dec):
    ls = list(value.keys())
    ls.sort(reverse=True)
    rem = dec 
    res = []
    while rem!=0:
        for i in range(len(ls)):
            if dec in ls:
                res.append(value[dec])
                rem = 0
                break
            if ls[i]<dec:
                quo = dec//ls[i]
                rem = dec%ls[i]
                res.append(value[ls[i]]*quo)
                break 
        dec = rem
    res = ''.join(res)
    return res
	
decimal = 3549
roman = decimalToRoman(decimal)
print(roman)