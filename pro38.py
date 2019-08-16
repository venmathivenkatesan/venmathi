ven,mathi=map(int,input().split())
anto=list(map(int,input().split()))
aaa=0
for j in anto:
    if j<=(5-mathi):
        aaa+=1
Gtee=aaa//3
print(Gtee)
