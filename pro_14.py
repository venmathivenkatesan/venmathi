v,n=map(int,input().split())
list1=list(map(int,input().split()))
v=[]
list1.insert(0,0)
for s in range(n):
     m=[]
     sumup=0
     aa,bb=map(int,input().split())
     for i in range(aa,bb+1):         
         sumup^=list1[i]     
     v.append(sumup)
for s in v:
    print(s)
