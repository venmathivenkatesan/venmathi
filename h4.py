V=int(input())
n1=input(" ")
n1=list(n1.split(' '))
c={}
for i in n1:
   if i in c:
      c[i]+=1
   else:
      c[i]=1
for key,value in c.items():
  if value==1:
     print(key)
