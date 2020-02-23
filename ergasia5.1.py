string=input('grapse to txt arxeio poy thes na anoikseis')
string=open(string+'.txt').read()
for x in string.split():
    if len(x)>3:
        x=x[1:]+x[0]+"ay"
        print(x)
    else:
        print(x)
