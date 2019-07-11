asd=int(input())
asd2=list(map(int,input().split()))
for q in range(len(asd2)-1):
     if(asd2[q]>asd2[q+1]):
           print(q)
           break
