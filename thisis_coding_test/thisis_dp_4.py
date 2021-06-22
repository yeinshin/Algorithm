#2부<문제>4번-바닥 공사

n = int(input())

dp = [1,3] + [0]*(n-2)

if n<=2:
    print(dp[n-1])
else:
    for i in range(2,n):
        dp[i]=dp[i-1]+dp[i-2]*1
    print(dp[n-1]%796796)

