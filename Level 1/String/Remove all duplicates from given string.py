def removeAllDuplicates(ip):
    count = {}
    for i in ip:
        if i not in count:
            count[i]=1 
        else:
            count[i]=count[i]+1 
    ip = list(ip)
    i = 0
    while i<len(ip):
        if count[ip[i]]>1:
            ip.pop(i)
        else:
            i=i+1 
    ip=''.join(ip)
    return ip

ip = "abcabaaa"
op = removeAllDuplicates(ip)
print(op)