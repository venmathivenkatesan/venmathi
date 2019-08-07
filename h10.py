ve,vi = map(int,input().split())
bo1 = list(map(int,input().split()))
bo2 = list(map(int,input().split()))
x =1
for k in bo2:
    if k not in bo1:
        print('NO')
        x = 0
        break
if(x):
    print('YES')# 
