def lcs(x,y,n,m):
    if n==0 or m==0:
        return 0
    if x[n-1] == y[m-1]:
        return 1+ lcs(x,y,n-1,m-1)
    else:
        return max(lcs(x,y,n-1,m),lcs(x,y,n,m-1))

x = "abcde"
y = "ace"
n = len(x)
m = len(y)
length = lcs(x,y,n,m)
print(length)