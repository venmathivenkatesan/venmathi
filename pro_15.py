vn=int(input())
det=list(map(int,input().split(" ")))
det=[bin(j) for j in det]
det.sort(reverse=True)
det=[int(vn,2) for vn in det]
for j in range(0,vn):
     print(det[j])
