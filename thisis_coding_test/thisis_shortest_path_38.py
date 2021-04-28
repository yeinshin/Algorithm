#3부<문제>38번-정확한 순위

import sys

INF = int(1e9)
input=sys.stdin.readline

#n:학생들의 수, m:두 학생의 성적을 비교한 횟수
n,m=map(int,input().split())

graph=[[INF]*(n+1) for _ in range(n+1)]

#자기 자신과의 성적은 비교 할 수 없으므로 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

#성적 비교한 학생 그래프 생성/ m은 두 학생의 성적을 비교한 횟수 이므로 m만큼 값 넣어준다
for _ in range(m):
    #두 학생의 성적을 비교한 결과를 나타내는 정수 a와 b
    a,b=map(int,input().split())
    graph[a][b]=1

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

#성적 순위를 정확히 알 수 있는 학생을 카운트할 리스트 생성
counts=[0]*n

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]!=INF and a!=b:
            counts[a-1]+=1
            counts[b-1]+=1

print(counts.count(n-1))
        