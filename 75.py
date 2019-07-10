gh2=list(input())
if len(gh2)%2==0:
    gh2[int(len(gh2)/2)] ='*'
    gh2[int(len(gh2)/2)-1]='*'
else:
    gh2[int(len(gh2)/2)] ='*'
for k in range(0,len(gh2)):
    print(gh2[k],end='')
