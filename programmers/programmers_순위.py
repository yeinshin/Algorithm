#https://programmers.co.kr/learn/courses/30/lessons/49191
#프로그래머스-순위/풀이 참고함

def solution(n, results):
    answer = 0
    graph = [[0]*n for _ in range(n)]
    
    for a,b in results:
        graph[a-1][b-1]=1
        graph[b-1][a-1]=-1
    
    for k in range(n):
        for a in range(n):
            for b in range(n):
                if graph[a][b]==0:
                    if graph[a][k]==1 and graph[k][b]==1:
                        graph[a][b]=1
                        graph[b][a]=-1
                    elif graph[a][k]==-1 and graph[k][b]==-1:
                        graph[a][b]=-1
                        graph[b][a]=1
        
    for i in range(n):
        if graph[i].count(0)==1:
            answer+=1
    
    return answer