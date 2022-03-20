def printNumbers(n):
    if n==1:
        print(1)
        return
    printNumbers(n-1)
    print(n)

printNumbers(5)