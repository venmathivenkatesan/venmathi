ab=int(input())
ven=list(map(int,input().split()))
for h in range(len(ven)-1):
   if(nums[h]>ven[h+1]):
      print(h)
