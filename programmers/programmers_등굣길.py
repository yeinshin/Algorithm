#https://programmers.co.kr/learn/courses/30/lessons/42898
#프로그래머스-등굣길
def solution(m, n, puddles):
    answer = 0
    dp = [[0]*(m+1) for _ in range(n+1)]    
    #집(시작좌표)-> (1,1)을 1로 변경
    dp[1][1]=1

    for i in range(1,n+1):
        for j in range(1,m+1):
            #집 좌표일때는 무시
            if (i,j)==(1,1):
                continue
            if [j,i] in puddles:
                dp[i][j]=0
            else: dp[i][j]=dp[i-1][j]+dp[i][j-1]                
    
    return dp[n][m]% 1000000007