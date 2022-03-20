op = 0
def reverseANumber(n):
    global op
    if n<10:
        op = op*10+n
        return
    op = op*10+n%10
    reverseANumber(n//10)

reverseANumber(3456)
print(op)