#https://programmers.co.kr/learn/courses/30/lessons/12907
#프로그래머스-거스름돈

def solution(n, money):
    answer = 0
    dp = [0]*100001
    dp[0]=1
    for m in money:
        for i in range(1,100001):
            if i-m>=0:
                dp[i]+=dp[i-m]
    
    return dp[n]