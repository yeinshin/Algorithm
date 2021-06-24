#https://www.acmicpc.net/problem/15989
#15989번-1,2,3 더하기 4/풀이 참고함

for _ in range(int(input())):
    n = int(input())

    dp = [[0,0,0,0] for _ in range(10001)]
    dp[1][1]=1
    
    dp[2][1]=1
    dp[2][2]=1
    
    dp[3][1]=1
    dp[3][2]=1
    dp[3][3]=1

    for i in range(4,10001):
        dp[i][1]+=dp[i-1][1]
        dp[i][2]= dp[i-2][1]+dp[i-2][2]
        dp[i][3]= dp[i-3][1]+dp[i-3][2]+dp[i-3][3]
    
    print(sum(dp[n]))

#-----------------------------------------------------------------------------------#
#다른 풀이

n = int(input())
d = [0] * 10001
nums = [1, 2, 3]
d[0] = 1
for j in range(3):
	for i in range(1, 10001):
		if i - nums[j] >= 0:
			d[i] += d[i - nums[j]]
             
for _ in range(n):
	a = int(input())
	print(d[a])