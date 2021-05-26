#https://www.acmicpc.net/problem/1987
#1987번-알파벳

r,c = map(int,input().split())
alpha = [list(map(lambda x: ord(x)-65,input())) for _ in range(r)]
visited = [False]*26
dx=[-1,1,0,0]
dy=[0,0,-1,1]

result = 1

def dfs(x,y,cnt):
    global result

    if x<=-1 or x>=r or y<=-1 or y>=c:
        return

    if not visited[alpha[x][y]]:

        visited[alpha[x][y]]=True
        dfs(x-1,y,cnt+1)
        dfs(x+1,y,cnt+1)
        dfs(x,y-1,cnt+1)
        dfs(x,y+1,cnt+1)

        visited[alpha[x][y]]=False
        result = max(result,cnt)

dfs(0,0,1)
print(result)