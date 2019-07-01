vv,vad=map(int,input().split())
for m in range(vv+1,vad,1):
    if(m>1):
        for n in range(2,m):
            if(m%n==0):
                break
        else:
            print(m,end=" ")
