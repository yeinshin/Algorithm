#https://www.acmicpc.net/problem/2023
#2023번-신기한 소수
import sys
input = sys.stdin.readline

#자릿수 입력받기
n = int(input())

#dfs 함수
def dfs(cnt,result):
    
    if cnt == n:
        print(*result,sep='')
        return

    for i in range(1,10):
        if check(cnt+1,result+[i]):
            result.append(i)
            dfs(cnt+1,result)
            result.pop()

#소수인지 check 해주는 함수
def check(cnt,num):

    num = int(''.join(map(str,num)))

    #현재까지 한자리 수 입력 받았을 때,
    if cnt==1:
        if num==2 or num ==3 or num==5 or num==7:
            return True
        return False

    #현재까지 자릿수가 두자리 이상일 때,
    else:
        for i in range(2,num):
            if num%i==0:
                return False
        return True

#dfs 실행
dfs(0,[])