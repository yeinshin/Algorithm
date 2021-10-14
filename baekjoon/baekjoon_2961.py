#https://www.acmicpc.net/problem/2961
#2961번-도영이가 만든 맛있는 음식
from itertools import combinations
n = int(input())
foods = [list(map(int,input().split())) for _ in range(n)]
result = int(1e9)
for i in range(1,n+1):
    for comb in combinations(range(n),i):
        s = 1
        ss = 0
        for c in comb:
            s*=foods[c][0]
            ss+=foods[c][1]
        result = min(result,abs(s-ss))
print(result)
