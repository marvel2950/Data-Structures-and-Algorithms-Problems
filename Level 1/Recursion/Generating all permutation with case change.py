def permutationWithCaseChange(ip,op):
    if len(ip)==0:
        print(op)
        return
    permutationWithCaseChange(ip[1:],op+ip[0].upper())
    permutationWithCaseChange(ip[1:],op+ip[0])

ip = 'ab'
op = ''
permutationWithCaseChange(ip,op)