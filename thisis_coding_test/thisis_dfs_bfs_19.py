#3부<문제>19번-연산자 끼워 넣기/다시 풀어보기 너무 어려워ㅠㅠㅠㅠㅠㅠㅠㅠ
#dfs를 이용한 풀이

import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))

#+,-,x,/ (덧셈,뺄셈,곱셈,나눗셈)
add,sub,mul,div = map(int,input().split())

max_value = -1e9
min_value = 1e9

def dfs(i,now):
    global min_value,max_value,add,sub,mul,div

    if i==n:
        min_value = min(min_value,now)
        max_value = max(max_value,now)

    else:
        #각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add-=1
            print("add-=1 실행 add:",add)
            print("전 i:",i)
            dfs(i+1,now + data[i])

            add+=1
            print("add+=1 실행 add:",add)
            print("후 i:",i)
        if sub > 0:
            sub-=1
            print("sub-=1 실행 sub:",sub)
            print("전 i:",i)
            dfs(i+1,now - data[i])
        
            sub+=1
            print("sub+=1 실행 sub:",sub)
            print("후 i:",i)
        if mul > 0:
            mul-=1
            print("mul-=1 실행 mul:",mul)
            print("전 i:",i)
            dfs(i+1,now * data[i])
            
            mul+=1
            print("mul+=1 실행 mul:",mul)
            print("후 i:",i)
        if div > 0:
            div-=1
            print("div-=1 실행 div:",div)
            print("전 i:",i)
            dfs(i+1,int(now / data[i])) #나눌 때는 나머지를 제거
            
            div+=1
            print("div+=1 실행 div:",div)
            print("후 i:",i)

dfs(1,data[0]) #dfs(i,now)

print("max_value:",max_value)
print("min_value:",min_value)
