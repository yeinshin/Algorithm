#https://www.acmicpc.net/problem/1719
#1719번-택배
n,m = map(int,input().split())
INF = int(1e9)
f = [[INF]*n for _ in range(n)]
test = [[0]*n for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,input().split())
    f[a-1][b-1]=c
    f[b-1][a-1]=c
    test[a-1][b-1]=b
    test[b-1][a-1]=a
for k in range(n):
    for a in range(n):
        for b in range(n):
            if f[a][b]>f[a][k]+f[k][b]: 
                test[a][b]=test[a][k]
                f[a][b]=f[a][k]+f[k][b]
for i in range(n):
    for j in range(n):
        if i==j: print('-',end=' ')
        else: print(test[i][j],end=' ')
    print()