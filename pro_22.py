num_N=int(input())
arr_N=list(map(int,input().split()))
even=[]
odd=[]
for j in range(len(arr_N)):
	if j%2==0:
		even.append(arr_N[j])
	else:
		odd.append(arr_N[j])
sum_even=sum(even)
sum_odd=sum(odd)
if(sum_even>sum_odd):
	print(sum_even)
else:
	print(sum_odd)
