m=int(input())
sum=0
temp=m
while temp>0:
   digit=temp%10
   sum += digit**3
   temp//=10
if m==sum:
   print("yes")
else:
   print("no")

