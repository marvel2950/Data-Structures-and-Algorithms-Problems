def reverse(ip_str):
    ip_str = list(ip_str)
    i = 0
    j = len(ip_str)-1
    while i<j:
        ip_str[i],ip_str[j] = ip_str[j],ip_str[i]
        i+=1
        j-=1
    ip_str = ''.join(ip_str)
    return ip_str

def checkPal1(ip_str):
    reverse_str = reverse(ip_str)
    if reverse_str==ip_str:
        return True 
    return False 

ip_str = 'abcba'
flag = checkPal1(ip_str)
print(flag)

def checkPal2(ip_str):
    i = 0
    j = len(ip_str)-1
    while i<j:
        if ip_str[i]!=ip_str[j]:
            return False
        i+=1
        j-=1
    return True

ip_str = 'abcbad'
flag = checkPal2(ip_str)
print(flag)