def minCoins(v,deno):
    deno.sort()
    n = len(deno)
    ans = []
    i = n-1 
    while i>=0:
        while v>=deno[i]:
            v -= deno[i]
            ans.append(deno[i])
        i-=1
    return ans

v = 93 
deno = [1,2000,500,2,10,20,50,100,5]
change = minCoins(v,deno)
print(change)