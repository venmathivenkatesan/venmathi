v1,v2=map(int,input().split())
v3=[]
for k in range(v1,v2+1):
    for p in range(2,k):
        if(k%p==0):
            break
    else:
        v3.append(k)
print(len(v3))
