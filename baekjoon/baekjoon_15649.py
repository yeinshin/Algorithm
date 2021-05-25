#https://www.acmicpc.net/problem/15649
#15649번-N과 M (1)
#itertools의 permutations를 이용한 풀이

from itertools import permutations

n,m = map(int,input().split())
permu = list(permutations(list(range(1,n+1)),m))

for p in permu:
    for i in range(m):
        print(p[i])