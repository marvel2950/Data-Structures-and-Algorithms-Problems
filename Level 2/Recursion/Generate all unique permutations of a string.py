def permute(s,l,r,per):
    if l==r:
        per.append(''.join(s))
    else:
        for i in range(l,r+1):
            s[i],s[l] = s[l],s[i]
            permute(s,l+1,r,per)
            s[i],s[l] = s[l],s[i]

def uniquePermute1(s,l,r):
    per = []
    permute(s,l,r,per)
    print(list(set(per)))

def check(s,l,cur):
    for j in range(l,cur):
        if s[j] == s[cur]:
            return False
    return True

def uniquePermute2(s,l,r):
    if l==r:
        print(''.join(s))
    else:
        for i in range(l,r+1):
            flag = check(s,l,i)
            if flag:
                s[i],s[l] = s[l],s[i]
                uniquePermute2(s,l+1,r)
                s[i],s[l] = s[l],s[i]

s = "aab"
s = list(s)
n = len(s)
uniquePermute1(s,0,n-1)
uniquePermute2(s,0,n-1)