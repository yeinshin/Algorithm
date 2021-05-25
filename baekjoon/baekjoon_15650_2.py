#https://www.acmicpc.net/problem/15650
#15650번-N과 M(2)
#itertools의 combinations를 이용한 풀이

from itertools import combinations

n,m = map(int,input().split())

for i in combinations(list(range(1,n+1)), m):
    print(*i)