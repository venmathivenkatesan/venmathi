ven=int(input())
nila=input().split()
for n in range(len(nila)):
    for i in range(n+1,len(nila)):
        for u in range(i+1,len(nila)):
            if(int(nila[n])+int(nila[i])==int(nila[u])):
                print(nila[n],nila[i],nila[u])
