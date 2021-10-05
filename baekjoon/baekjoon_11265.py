#https://www.acmicpc.net/problem/11265
#11265번-끝나지 않는 파티

n,m = map(int,input().split())
floyd = [list(map(int,input().split())) for _ in range(n)]

for k in range(n):
    for a in range(n):
        for b in range(n):
            floyd[a][b]=min(floyd[a][b],floyd[a][k]+floyd[k][b])

for _ in range(m):
    a,b,c = map(int,input().split())
    print('Enjoy other party' if floyd[a-1][b-1]<=c else 'Stay here')