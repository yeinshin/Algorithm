#https://www.acmicpc.net/problem/16943
#16943번-숫자 재배치
from itertools import permutations
a,b = input().split()
b = int(b)
ans = -1
for i in permutations(a):
    number = int(''.join(i))
    if number<b and len(i)==len(str(number)): 
        ans = max(ans,number)
print(ans)