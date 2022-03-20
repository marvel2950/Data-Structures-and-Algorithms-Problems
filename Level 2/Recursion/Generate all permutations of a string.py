import itertools

class Solution:
    def permute(self,s,l,r):
        if l==r:
            print(''.join(s))
        else:
            for i in range(l,r+1):
                s[i],s[l] = s[l],s[i]
                self.permute(s,l+1,r)
                s[i],s[l] = s[l],s[i]

    def permute(self,s):
        n = len(s)
        for i in itertools.permutations(s,n):
            print(''.join(i))

s = "aab"
s = list(s)
n = len(s)
sol = Solution()
sol.permute(s)
print()
#sol.permute(s,0,n-1)