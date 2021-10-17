#https://www.acmicpc.net/problem/18511
#18511번-큰 수 구성하기
from itertools import product
n,k = map(str,input().split())
nums = list(map(int,input().split()))
result = 0
first = 0
for num in nums:
    if int(n[0])>=num: first = max(first,num)
test = list(product(list(map(str,nums)),repeat=len(n)-1))
for t in test:
    now = int(str(first)+''.join(t))
    if now<=int(n):
        result = max(result,now)
print(result)

    