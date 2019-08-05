num=int(input())
m=list(map(int,input().split()))
v=[]
for l in range(num):
    if m[l]==l:
        v.append(str(m[l]))
        v.sort()
if len(v)==0:
    print("-1")
else:
    print(" ".join(v))
