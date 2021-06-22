#https://www.acmicpc.net/problem/1699
#1699번-제곱수의 합/풀이 참고함

n = int(input())
 
dp = list(range(n+1))

for i in range(1,n+1):
    #제곱근 for 문
    for j in range(1,i):
        if j*j>i:
            break
        if dp[i]>dp[i-j*j]+1:
            dp[i] = dp[i-j*j]+1
            
print(dp[n])