#10819번-차이를 최대로

from itertools import permutations

n=int(input())
array = list(map(int,input().split()))

perm = list(permutations(array,n))

max_result=0

for p in perm:
    result=0
    for i in range(n-1):
        result+=abs(p[i]-p[i+1])
    
    max_result = max(max_result,result)

print(max_result)

