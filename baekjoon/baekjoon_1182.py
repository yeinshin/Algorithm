#1182번-부분수열의 합

from itertools import combinations

n,s = map(int,input().split())

numbers = list(map(int,input().split()))
cnt = 0
for i in range(1,len(numbers)+1):
    comb = list(combinations(numbers,i))

    for c in comb:
        if s==sum(c):
            cnt+=1
print(cnt)