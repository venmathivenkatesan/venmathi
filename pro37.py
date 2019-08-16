ven=int(input())
pop=list(map(int,input().split()))
vv=0
mmm=0
while(mmm<len(pop)):
    tat=pop[mmm]
    if(mmm==0):
        if(len(pop)==1):
            vv=1 
            break
    elif(mmm==len(pop)-1):
        vv=vv
    else:
        if(tat>pop[mmm+1] and tat>pop[mmm-1]):
            vv=vv+1
        elif(tat<pop[mmm-1] and tat<pop[mmm+1]):
            vv=vv+1
    mmm=mmm+1
print(vv)
