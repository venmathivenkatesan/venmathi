v=int(input())
v=list(map(int,input().split()))
v.sort()
v.reverse()
if v[0]==0:
    print("0")
else:
    for l in v:
        print(l,end='')
