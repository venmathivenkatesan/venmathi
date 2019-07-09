ven=int(input(""))
vm=list(map(int,input("").split()[:ven]))
sum=0
for j in range(0,ven):
    sum=sum+vm[j]
print(sum//ven)
