V_coin,sum_coin=list(map(int,input().split()))
ab_coin=list(map(int,input().split()))
ab_coin.sort(reverse=True)
cd=0
for j in ab_coin:
    if sum_coin==0:
        break
    qt=sum_coin // j
    cd+=qt
    sum_coin=sum_coin-j*qt
print(cd)
