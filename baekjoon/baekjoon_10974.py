#https://www.acmicpc.net/problem/10974
#10974번-모든 순열

from itertools import permutations

n=int(input())
l = list(range(1,n+1))
l = sorted(list(permutations(l,n)))

for i in l:
    for j in range(n):
        print(i[j],end=' ')
    print()