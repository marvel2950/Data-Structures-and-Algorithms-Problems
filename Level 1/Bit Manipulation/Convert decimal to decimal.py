def decimalToBinary1(num):
    bin_num = []
    while num>=1:
        bin_num.append(str(num%2))
        num = num//2 
    bin_num.reverse()
    return ''.join(bin_num)

def decimalToBinary2(num,bin_num):
    if num>=1:
        decimalToBinary2(num//2,bin_num)
    bin_num.append(str(num%2))
 

dec_num = 22 

bin_num = decimalToBinary1(dec_num)
print(bin_num)

bin_num = []
decimalToBinary2(dec_num,bin_num)
bin_num = ''.join(bin_num)
print(bin_num)

bin_num = bin(dec_num)[2:]
print(bin_num)
