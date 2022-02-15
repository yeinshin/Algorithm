#https://www.acmicpc.net/problem/4803
#4803번-트리
import sys
input = sys.stdin.readline

def dfs(prev, node):
    visited[node] = True
    for n in graph[node]:
        #graph 배열에서는 연결된 노드를 전체 저장하므로 이전에 방문한 노드를 사이클로 인식할 수 도 있다.
        #이를 방지하기 위해 다음 노드와 이전 노드가 같은지 확인하는 작업을 추가한다.
        if n == prev:
            continue
        #이미 방문한 경우 사이클이 생기므로 트리가 아님
        if visited[n]:
            return False
        if not dfs(node, n):
            return False
    return True

tc = 0
while True:
    tc += 1
    N, M = map(int, input().split())
    if [N, M] == [0, 0]: 
        break
    graph = [[] for _ in range(N+1)] 
    visited = [False] * (N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b) 
        graph[b].append(a)

    cnt = 0 # 트리의 개수
    for v in range(1, N+1):
        if not visited[v]:
            if dfs(0, v):
                cnt += 1
    if cnt == 0:
        print("Case {}: No trees.".format(tc))
    elif cnt == 1:
        print("Case {}: There is one tree.".format(tc))
    else:
        print("Case {}: A forest of {} trees.".format(tc, cnt))


#bfs를 사용한 풀이
# from collections import deque
# def bfs(i):
#     q=deque([(i,-1)])
#     while q:
#         u, prev = q.popleft()
#         visit[u]=1
#         for v in adj[u]:
#             if v == prev: continue
#             if visit[v]: return 0   #cycle
#             q.append((v,u))
#     return 1
# case=1
# while 1:
#     n,m=map(int,input().split())
#     if n==0 and m==0:break
#     adj=[[]for _ in range(n)]
#     for i in range(m):
#         a,b=map(int,input().split())
#         a-=1;b-=1
#         adj[a].append(b)
#         adj[b].append(a)
#     visit=[0]*n
#     res=0
#     for i in range(n):
#         if not visit[i]:
#             res+=bfs(i)
#     if not res:print('Case {}: No trees.'.format(case))
#     elif res == 1: print('Case {}: There is one tree.'.format(case))
#     else: print('Case {}: A forest of {} trees.'.format(case, res))
#     case+=1
