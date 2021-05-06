#2부<문제>3번-음료수 얼려 먹기/다시 풀어보기

n,m = map(int,input().split())

graph = [list(map(int,input())) for _ in range(n)]

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# visited = [[True]*(m) for _ in range(n)]

def dfs(x,y):

    if x>=n or x<0 or y>=m or y<0:
        return False
    
    #현재 노드를 방문하지 않았다면
    if graph[x][y]==0:
        
        graph[x][y]=1

        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)    

        return True 
    
    return False


# result = 0 

# for x in range(n):
#     for y in range(m):
#         if dfs(x,y)== True:
#             result+=1