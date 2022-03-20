def firstNonRepeating(ip):
    count = {}
    for i in ip:
        if i not in count:
            count[i] = 1
        else:
            count[i] = count[i]+1 
    ans = ''
    for i in ip:
        if count[i]==1:
            ans = i 
            break 
    return ans


ip = "abccabaaadd"
op = firstNonRepeating(ip)
print("Op",op)