#https://www.acmicpc.net/problem/2026
#2026번-소풍(풀이참고)
import sys
input = sys.stdin.readline

def backtracking(now,arr,cnt):
    global K,N
    if cnt==K:
        print(*arr,sep='\n')
        sys.exit(0)
    
    for i in range(now+1,N+1):
        for a in arr:
            # graph[i]에 a가 포함되어있다면 -> graph[a]에도 i가 포함되어있다. 양방향이기때문에
            if a not in graph[i]:
                break
        else:
            backtracking(i,arr+[i],cnt+1)

K, N, F = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(F):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N+1):
    backtracking(i,[i],1)

print(-1)