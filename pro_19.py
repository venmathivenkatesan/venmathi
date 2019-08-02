no_elm=int(input())
ven_arr=[]
for j in range(no_elm):
	elm=list(map(int,input().split(" ")))
	for k in range(len(elm)):
		ven_arr.append(elm[k])
ven_arr.sort()
print(*ven_arr,sep=" ")
