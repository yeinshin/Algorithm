#https://www.acmicpc.net/problem/14248
#14248번-점프 점프
n = int(input())
rocks = list(map(int,input().split()))
now = int(input())
visited = [0]*n
def dfs(num):
    global n
    visited[num]=1
    for i in (num-rocks[num],num+rocks[num]):
        if 0<=i<n and visited[i]==0:
            dfs(i)

dfs(now-1)
print(sum(visited))