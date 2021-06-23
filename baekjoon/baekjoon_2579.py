#https://www.acmicpc.net/problem/2579
#2579번-계단 오르기/풀이 참고함

n = int(input())
s = list(int(input()) for _ in range(n))+[0]*(300-n)
dp = [0 for i in range(300)]
dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1] + s[2], s[0] + s[2])
for i in range(3, n):
    dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
print(dp[n - 1])