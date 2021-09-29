#https://www.acmicpc.net/problem/2805
#2805번-나무 자르기/풀이참고
n,m = map(int,input().split())
tree = list(map(int,input().split()))
start,end = 0,max(tree)
while start<=end:
    mid = (start+end)//2
    plus= sum([t-mid if t> mid else 0 for t in tree])
    if plus>=m: start=mid+1
    else: end=mid-1
print(end)