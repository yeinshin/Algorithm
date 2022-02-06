#https://www.acmicpc.net/problem/2493
#2493번-탑

import sys
input = sys.stdin.readline
n = int(input())
tops = list(map(int,input().split()))
ans = [0]*n
check = []

for i in range(n-1,0,-1):
    check.append(i)
    while check:
        if tops[check[-1]]<tops[i-1]: 
            ans[check[-1]]=i
            check.pop()
        else: break
print(*ans)