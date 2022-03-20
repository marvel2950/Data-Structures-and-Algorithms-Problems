def printNumbers(n):
    if n==1:
        print(1)
        return
    print(n)
    printNumbers(n-1)
printNumbers(8)