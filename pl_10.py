vi=input()
vi=vi.split()
ven=vi[0]
y=vi[1]
count=0
k=0
while(k<len(ven) and count<2):
    if(san[k]!=y[k]):
        count+=1
    k+=1
if(count==1 or count==0):
    print("yes")
else:
    print("no")
