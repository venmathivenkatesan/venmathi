v_inp=(input())
inp=0
for j in range(0,len(v_inp)):
    n_inp=(v_inp[:j]+v_inp[j+1:])
    if(int(n_inp) % 8==0):
        inp=1
        break
if(inp==1):
    print("yes")
else:
    print("no")
