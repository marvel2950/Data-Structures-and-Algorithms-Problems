import math
def factors1(n):
    factors_list = []
    i = 1
    while i<=n:
        if n%i==0:
            factors_list.append(i)
        i=i+1 
    return factors_list


n = 18
factors_list = factors1(n)
print(factors_list)

def factors2(n):
    factors_list1 = []
    factors_list2 = []
    i = 1
    while i<=math.sqrt(n):
        if n%i==0:
            if n/i==i:
                factors_list1.append(i)
            else:
                factors_list1.append(i)
                factors_list2.append(n//i)
        i=i+1 
    factors_list2.reverse()
    factors_list1.extend(factors_list2)
    return factors_list1


n = 100
factors_list = factors2(n)
print(factors_list)