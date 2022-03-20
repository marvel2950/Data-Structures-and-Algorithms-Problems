#Iterative approach
def factorial_itertive(n):
    fact = 1
    for i in range(n,0,-1):
        fact=fact*i 
    return fact

#Recursive approach
def factorial_recursive(n):
    if n==1:
        return 1
    return n*factorial_recursive(n-1)


n = 5
fact1 = factorial_itertive(n)
print(fact1)

fact2 = factorial_recursive(n)
print(fact2)