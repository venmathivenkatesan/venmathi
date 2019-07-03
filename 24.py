get=int(input())
il=list(map(int,input().split()[:get]))
il.sort()
for p in il:
        print(p,end=" ")
