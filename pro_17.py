V_17=list(map(int,input().split()))
vm1=V_17[1]
flag1=0
c_17=list(map(int,input().split()))
for k in range(0,len(c_17)-1):
	for j in range(k+1,len(c_17)):
		if c_17[k]+c_17[j]==vm1:
			print("yes")
			flag1=1
			break
	if flag1==1:
		break
if flag1!=1:
	print("no")
