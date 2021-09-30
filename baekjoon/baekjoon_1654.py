#https://www.acmicpc.net/problem/1654
#1654번-랜선 자르기
k,n =map(int,input().split())
tree = [int(input()) for _ in range(k)]
start,end = 1,max(tree)
while start<=end:
    mid = (start+end)//2
    s = sum([t//mid for t in tree])
    if s>=n:start=mid+1
    else: end = mid-1
print(end)