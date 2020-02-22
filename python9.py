print("grapse arithmo")
a=int(input())
s=0
a=(a*3)+1
d=10
print(a)
print("pollaplasiastike *3 kai prostethike +1")
while a!=0:
    s+=a%10
    a=int(a/10)
    if a==0 and int(s/10)!=0:
        a=s
        s=0
        a=(a*3)+1
        continue
print(s)
print("teliko apotelesma")
    

   
    
                

