mathi = int(input())
ven = [ int(p) for p in input().split()]
mathi = len(ven)
anto = 0
for aa in range(0,mathi-2):
    for bb in range(aa+1, mathi-1):
        for cc in range(bb+1, mathi):
            if ven[aa] > ven[bb] > ven[cc] :
               anto =anto+ 1
print(anto)
