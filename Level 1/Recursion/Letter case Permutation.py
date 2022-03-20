def letterCasePermutation(ip,op):
    if len(ip)==0:
        print(op)
        return 

    if ip[0] in '1234567890':
        letterCasePermutation(ip[1:],op+ip[0])
    else:
        letterCasePermutation(ip[1:],op+ip[0])
        letterCasePermutation(ip[1:],op+ip[0].upper())

ip = 'a1b2'
op = ''
letterCasePermutation(ip,op)