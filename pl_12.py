v,s=map(int,input().split())
c=list(map(int,input().split()))
for j in range (0,s):
    c=[c[-1]]+c[:-1]
print(*c,end='')
