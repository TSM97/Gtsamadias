s=''
cnt=0
while True:
   cnt=0
   s=input("type something\n")
   if s=='stop':
      break
   x=(''.join(str(ord(c)) for c in s))
   print(x)
   x=int(x)
   for i in range(x):      
     if x%(i+1)==0:
        cnt+=1
   else:
     if cnt==2:
        print("o arithmos einai prwtos")
     if cnt!=2:
        print("o arithmos den einai prwtos")
quit()   
