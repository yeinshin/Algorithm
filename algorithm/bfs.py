#BFS 알고리즘 예제 소스코드

from collections import deque

#BFS 메서드 정의
def bfs(graph,start,visited):
    #큐 구현을 위해 deque 라이브러리 사용
    q = deque([start])
    #현재 노드를 방문 처리
    visited[start] = True

    #큐가 빌 때까지 반복
    while q:
        #큐에서 하나의 원소를 뽑아 출력
        v = q.popleft()
        print(v,end =' ')
        #해당 원소와 연결된 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i]=True

#노드 수 입력받기
n=int(input())

#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph=[[] for _ in range(n+1)]

#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False]*9

bfs(graph,1,visited)



