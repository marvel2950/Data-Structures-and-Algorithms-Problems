def compression(ip_str):
    if len(ip_str)==0:
        return ''
    last = ip_str[0]
    c = 1
    op = []
    for i in range(1,len(ip_str)):
        if ip_str[i]==last:
            c=c+1 
        else:
            op.append(last)
            op.append(str(c))
            last = ip_str[i]
            c = 1 
    op.append(last)
    op.append(str(c))
    op = ''.join(op)
    return op

ip_str = 'aabcccccaaa'
op = compression(ip_str)
print(op)