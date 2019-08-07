v,k1=map(int,input().split())

paa=list(map(int,input().split()))

vaa=list(map(int,input().split()))

tr1=[]

caa=0

for b in range(j):

    xr1=vaa[b]/paa[b]

    tr1.append(xr1)

while k1>=0 and len(tr1)>0:

    mindex=tr1.index(max(tr1))

    if k1>=paa[mindex]:

        caa=caa+vaa[mindex]

        k1=k1-paa[mindex]

    paa.pop(mindex)

    vaa.pop(mindex)

    tr1.pop(mindex)

print(caa)
