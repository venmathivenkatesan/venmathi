v_inp=int(input())
a_inp=[int(st) for st in input().split()]
a_inp.sort()
srt=0
ven=0
for j in range(len(a_inp)):
    if a_inp[j]>=srt:
        ven+=1
    srt=srt+a_inp[j]
print(ven)
