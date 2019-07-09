vm,g=map(int,input().split())
p=list(map(int,input().split()[:vm]))
count=0
for j in range(0,vm):
    if(p[j]==g):
        count=count+1
print(count)
