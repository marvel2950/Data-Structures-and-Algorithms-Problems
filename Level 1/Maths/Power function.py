def pow1(x,n):
    ans = 1
    flag = False
    if n<0:
        n = n*-1 
        flag = True
    for i in range(1,n+1):
        ans = ans*x 
    if flag==True:
        ans = 1/ans
    return ans 

def pow2(x,n):
    ans = 1 
    flag = False
    if n<0:
        n = n*-1 
        flag = True
    while n>0:
        if n%2==1:
            ans = ans*x 
            n = n-1
        else:
            x = x*x 
            n = n//2
    if flag==True:
        ans = 1/ans
    return ans

x = 5
n = -4
ans = pow1(x,n)
print(ans)

ans = pow2(x,n)
print(ans)

