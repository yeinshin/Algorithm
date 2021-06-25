#https://www.acmicpc.net/problem/11058
#11058번-크리보드/풀이 참고함

n = int(input())
dp = list(range(n+1))

for i in range(7,n+1):
    dp[i] = max(dp[i-3]*2,dp[i-4]*3,dp[i-5]*4)

print(dp[n])

