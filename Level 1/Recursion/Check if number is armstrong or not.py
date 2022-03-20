len = 0
def lengthOfANumber(num):
    global len
    if num<10:
        len=len+1
        return
    len=len+1
    lengthOfANumber(num//10)

value = 0
def armstrongValue(num,len):
    global value
    if num<10:
        value=value+(num%10)**len
        return     
    value=value+(num%10)**len
    armstrongValue(num//10,len)



num = 1531
lengthOfANumber(num)
armstrongValue(num,len)

if value==num:
    print("Armstrong number")
else:
   print("Not a armstrong number") 