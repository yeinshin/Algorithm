#https://www.acmicpc.net/problem/15651
#15651번-N과 M(3)
#itertools의 product을 이용한 풀이

from itertools import product

n,m = map(int,input().split())

for i in product(list(range(1,n+1)),repeat=m):
    print(*i)