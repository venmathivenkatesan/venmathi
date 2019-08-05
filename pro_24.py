v=int(input())
n=pow(2,v)
arr=[]
for j in range(n):  
    mt1=bin(j).replace("0b","")
    arr.append(mt1.zfill(v))
    arr.sort(key=(lambda x:x.count('1')))
for j in arr:
    print(j)
