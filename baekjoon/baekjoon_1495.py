#https://www.acmicpc.net/problem/1495
#1495번-기타리스트

n,s,m = map(int,input().split())

volume = list(map(int,input().split()))

dp = [[False]*(m+1) for _ in range(n+1)]
dp[0][s]=True

for i in range(1,n+1):
    for j in range(m+1):
        if dp[i-1][j]:
            if j-volume[i-1]>=0:
                dp[i][j-volume[i-1]]=True
            if j+volume[i-1]<=m:
                dp[i][j+volume[i-1]]=True

result = False
for i in range(m,-1,-1):
    if dp[-1][i]:
        result = True
        print(i)
        break

if not result:print(-1)
