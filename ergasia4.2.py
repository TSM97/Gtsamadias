s=''
while True:
   s=input("type something\n")
   if s=='stop':
      break
   x=(''.join(str(ord(c)) for c in s))
   print(x)
   intx=int(x)
   if intx%2==1:
       print('o arithmos einai prwtos\ngrapse stop gia na stamatiseis')
   else:
     print('o arithmos den einai prwtos\ngrapse stop gia na stamatiseis')
quit()     
   




