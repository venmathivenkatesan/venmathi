from itertools import combinations
number ,vm = input().split()
vm = int(vm)
nila = []
hj = combinations(number,len(number)-vm)
for d in hj:
    nila.append("".join(d))
print(min(nila))
