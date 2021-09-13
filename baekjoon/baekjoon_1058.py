#https://www.acmicpc.net/problem/1058
#1058번-친구

n = int(input())
friend = [list(input()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i!=j and (friend[i][j]=='Y' or (friend[i][k]=='Y' and friend[k][j]=='Y')):
                visited[i][j]=True
answer = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if visited[i][j]: cnt+=1  
    answer= max(answer,cnt)
print(answer)