#1697번-숨바꼭질/다시 풀어보기

# 접근 방법
# 거리 이동 비용이 1인 경우, 특정 위치에서 특정 위치까지 가장 빠른 시간을 구하는 것은 가장 빠른 거리를 구하는 것과 같다. 비용이 1인 그래프 최소 거리는 BFS로 풀이할 수 있으므로 BFS로 접근했다.
# cf) 앞으로 문제가 그래프이론처럼 보이지 않아도 이동하는 문제에서 이동 비용이 1이면 그래프 그래프 이론을 고려해보자.

# 해결
# BFS는 로직상 꺼내는 순간 첫 방문일 경우 그 값이 최소 값으로 정해진다는 점을 이용한다.

import sys
from collections import deque

n,k = map(int, sys.stdin.readline().split())
visited = [0] * 100001

def solve(visited, n, k):
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()

        if x == k:
            return visited[x]

        for nx in (x+1, x-1, 2*x):
            if 0 <= nx < 100001 and visited[nx] == 0:
                visited[nx] = visited[x] + 1
                queue.append(nx)

print(solve(visited,n,k))
print(visited[:k+1])