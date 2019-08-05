v=input()
n=list(map(int,input().split()))
maximum=0
j=0
while(j<len(n)-1):
    count=0
    while(j<len(n)-1 and n[j]<n[j+1]):
        count+=1
        j+=1
    if(count>maximum):
        maximum=count
    j+=1
print(maximum+1)
