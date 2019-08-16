mathi,pop=map(int,input().split())
lst=[]
for _ in range(mathi):
	lst.append(sorted(list(map(int,input().split()))))
for i in range(mathi-1):
	for j in range(pop):
		for k in range(mathi-i):
			if(lst[i][j]>lst[i+k][j]):
				lst[i][j],lst[i+k][j]=lst[i+k][j],lst[i][j]
for i in lst:
	print(*i,sep=' ')    
