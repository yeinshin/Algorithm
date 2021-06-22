#2부<문제>2번-1로 만들기
#잘 알려진 다이나믹 프로그래밍 문제

x = int(input())
dp = [0]*30001

#Bottom-up 방식
for i in range(2,x+1):
    dp[i]=dp[i-1]+1

    if i%5==0 and dp[i]>dp[i//5]+1:
        dp[i] = min(dp[i],dp[i//5]+1)
    if i%3==0 and dp[i]>dp[i//3]+1:
        dp[i] = min(dp[i],dp[i//3]+1)
    if i%2==0 and dp[i]>dp[i//2]+1:
        dp[i] = min(dp[i],dp[i//2]+1)
print(dp[x])