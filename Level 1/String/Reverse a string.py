#1st approach
def reverse1(ip_str):
    op_str = '*'*len(ip_str)
    ip_str = list(ip_str)
    op_str = list(op_str)

    j = 0
    for i in range(len(ip_str)-1,-1,-1):
        op_str[j] = ip_str[i]
        j=j+1
    op_str = ''.join(op_str)
    return op_str

ip_str = 'akarsh'
ip_str = reverse1(ip_str)
print(ip_str)


#2st approach
def reverse2(ip_str):
    ip_str = list(ip_str)
    i = 0
    j = len(ip_str)-1
    while i<j:
        ip_str[i],ip_str[j] = ip_str[j],ip_str[i]
        i+=1
        j-=1
    ip_str = ''.join(ip_str)
    return ip_str
    
ip_str = 'akarsh'
ip_str = reverse2(ip_str)
print(ip_str)