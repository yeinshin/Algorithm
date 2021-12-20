#https://www.acmicpc.net/problem/3085
#3085번-사탕 게임
#NxN

n=int(input())
candy = [[s for s in input()] for _ in range(n)]

#swap

def check(i,j):
    
    check = ''
    cnt = 0
    max_cnt = 0
    # i행에 있는 요소들 검사
    for y in range(n):
        if check==candy[i][y]:
            cnt+=1
        else:
            check = candy[i][y]
            cnt = 1
        max_cnt = max(max_cnt,cnt)

    cnt = 0 
    check = ''
    # j열 , j+1열에 있는 요소들 검사
    for x in range(n):
        if check == candy[x][j]:
            cnt+=1
        else:
            check = candy[x][j]
            cnt = 1
        max_cnt = max(max_cnt,cnt)

    cnt = 0
    check = ''
    for x in range(n):
        if check == candy[x][j+1]:
            cnt+=1
        else:
            check = candy[x][j+1]
            cnt=1
        max_cnt = max(max_cnt,cnt)

    return max_cnt



def check_2(i,j):

    check = ''
    cnt = 0
    max_cnt = 0

    # j열에 있는 요소들 검사
    for x in range(n):
        if check==candy[x][j]:
            cnt+=1
        else:
            check = candy[x][j]
            cnt = 1
        max_cnt = max(max_cnt,cnt)

    cnt = 0 
    check = ''
    # i행, i+1열에 있는 요소들 검사
    for y in range(n):
        if check == candy[i][y]:
            cnt+=1
        else:
            check = candy[i][y]
            cnt = 1
        max_cnt = max(max_cnt,cnt)
    
    cnt = 0
    check = ''
    for y in range(n):
        if check == candy[i+1][y]:
            cnt+=1
        else:
            check = candy[i+1][y]
            cnt = 1
        max_cnt = max(max_cnt,cnt)

    return max_cnt


result = 0
temp = 0

for i in range(n):
    for j in range(n):
        #같은 행 다른 열끼리 swap
        if j+1<n:
            #좌우 교환
            candy[i][j],candy[i][j+1] = candy[i][j+1],candy[i][j]
            temp = check(i,j)
            
            if temp>result:
                result= temp

            #원상태로 복귀
            candy[i][j],candy[i][j+1] = candy[i][j+1],candy[i][j]

        #같은 열 다른 행끼리 swap
        if i+1<n:
            #상하 교환
            candy[i][j],candy[i+1][j] = candy[i+1][j],candy[i][j]
            temp = check_2(i,j)

            if temp>result:
                result= temp
            
            #원상태로 복귀
            candy[i][j],candy[i+1][j] = candy[i+1][j],candy[i][j]

print(result)


        


