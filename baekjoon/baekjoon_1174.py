#https://www.acmicpc.net/problem/1174
#1174번-줄어드는 숫자
from itertools import combinations
n= int(input())
result = []
for i in range(1,11):
    for comb in combinations(range(0,10),i):
        result.append(int(''.join(map(str,sorted(comb,reverse = True)))))
print(sorted(result)[n-1] if n<len(result) else -1)