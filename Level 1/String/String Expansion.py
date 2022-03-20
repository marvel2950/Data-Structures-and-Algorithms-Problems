def expansion(ip_str):
    if len(ip_str)<=1 or len(ip_str)%2!=0:
        return ''
    op = []
    for i in range(0,len(ip_str),2):
        chr = ip_str[i]
        count = int(ip_str[i+1])
        for j in range(count):
            op.append(chr)
    op = ''.join(op) 
    return op


ip_str = "a2b1c5a3"
op = expansion(ip_str)
print(op)