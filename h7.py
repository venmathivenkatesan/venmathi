h1=int(input())
m=list(map(int,input().split()[:h1]))
for i in range(len(m)):
    if((i%2==0)and(m[i]%2!=0)or(i%2!=0)and(m[i]%2==0)):
        print(m[i],end=" ")
