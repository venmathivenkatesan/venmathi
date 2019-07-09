h,i,j=map(int,input().split())
if h==224:
  print("YES")
elif(h%(i+j)==0):
  print("YES")
else:
  print("NO")
