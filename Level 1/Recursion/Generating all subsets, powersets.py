def subsetOfAString(ip,op):
    if len(ip)==0:
        print("String",op)
        return 
    subsetOfAString(ip[1:],op+ip[0])
    subsetOfAString(ip[1:],op)

ip = 'abc'
op = ''
subsetOfAString(ip,op)