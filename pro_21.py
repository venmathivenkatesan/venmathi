mathi_arr=int(input())
put_list=list(map(int,input().split()))[:mathi_arr]
div=int(mathi_arr/2)
abc_arr1=sum(put_list[:div])//len(put_list[:div])
abc_arr2=sum(put_list[div:])//len(put_list[div:])
if(abc_arr1==abc_arr2):
  print("yes")
else:
  print("no")
