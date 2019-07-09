vm=int(input())
p=[]
dif=0
for g in range (0,vm+1):
    dif=abs((2**g)-vm)
    p.append(dif)
sd=min(p)
print(sd)
