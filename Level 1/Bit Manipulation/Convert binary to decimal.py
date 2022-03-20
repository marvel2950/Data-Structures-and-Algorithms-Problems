def binaryToDecimal(num):
    dec_num = 0
    for i in range(len(num)):
        if num[i]=='1':
            x = (2*int(num[i]))
            n = len(num)-1-i 
            dec_num = dec_num + x**n
    return dec_num

bin_num = '10110'

dec_num = binaryToDecimal(bin_num)
print(dec_num)

dec_num = int(bin_num,2)
print(dec_num)
