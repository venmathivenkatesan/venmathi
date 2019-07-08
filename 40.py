ven=int(input())
kj1,df2=0,1
print(df2,end=" ")
for a in range(1,ven):
  fibo=kj1+df2
  print(fibo,end=" ")
  kj1,df2=df2,fibo
