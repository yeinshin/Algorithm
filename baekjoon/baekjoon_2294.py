#https://www.acmicpc.net/problem/2294
#2294번-동전 2

n,k = map(int,input().split())
array = list(int(input()) for _ in range(n))
dp = [10000]*(k+1)
dp[0]=0
for i in range(1,k+1):
    for a in array:
        if i-a>=0:
            dp[i]=min(dp[i],dp[i-a]+1)

if dp[k]!=10001:
    print(dp[k])
else:
    print(-1)