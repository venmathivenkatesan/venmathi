v_inp = int(input())
n_inp = int(v_inp/2)
arr = []
for i in range(v_inp, n_inp, -1):
    j = str(i)
    if i + sum([int(ven) for ven in j]) == v_inp:
        print(1)
        print(i)
        break
else:
    print(0) 


