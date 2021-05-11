#프로그래머스-네트워크
#DFS 풀이

def dfs(now,visited,computers,n):
    
    visited[now] = True
    
    for j in range(n):
        if computers[now][j]==1 and visited[j]==False and now!=j:
            dfs(j,visited,computers,n)
            
def solution(n, computers):
    
    answer = 0
    visited = [False]*n
    
    for i in range(n):
        if visited[i]==False:
            dfs(i,visited,computers,n)        
            answer+=1
        
    return answer