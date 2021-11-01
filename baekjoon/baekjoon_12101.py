#https://www.acmicpc.net/problem/12101
#12101번-1,2,3 더하기 2
from itertools import product
nums = [1,2,3]
n,k = map(int,input().split())
result = set()
for i in range(1,n+1):
    for p in product(nums,repeat = i):
        if sum(p)==n: result.add(tuple(map(str,p)))
if len(result)>=k:print(*(sorted(result)[k-1]),sep='+')
else:print(-1)