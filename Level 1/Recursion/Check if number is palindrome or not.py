op = 0
def reverseANumber(num):
    global op 
    if num<10:
       op=op*10+num%10 
       return
   
    op=op*10+num%10
    reverseANumber(num//10)

num = 3443
reverseANumber(num)

if op==num:
    print("Palindrome number")
else:
    print("Not a palindrome")