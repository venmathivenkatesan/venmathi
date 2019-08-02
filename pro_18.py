mat_row,mat_col=map(int,input().split())
ven=[]
for _ in range(mat_row):
    ven.append(input())
for ic in range(len(ven)):
    if('0' in ven[ic]):
        ven[ic]=ven[ic].replace('0','')
    ven[ic]=ven[ic].replace(' ','')
lengths=[]
for ic in ven:
    if(len(ic)>0):
        lengths.append(len(ic))
mat_col=min(lengths)
vn1='1 '*mat_col
vn1=vn1.strip()
for ic in range(mat_col):
    print(vn1)
