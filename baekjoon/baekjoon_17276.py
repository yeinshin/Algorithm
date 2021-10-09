#https://www.acmicpc.net/problem/17276
#17276번-배열 돌리기

for _ in range(int(input())):
    n,m = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(n)]
    
    if n!=1:
        for _ in range(abs(m)//45):
            a,b,c,d = list(map(list,zip(*graph)))[n//2],graph[n//2][:],[],[] #↓,→,↘,↗
            for i in range(n):
                c.append(graph[i][i])
                d.append(graph[n-i-1][i])
            if m<0: #왼쪽으로 회전
                for i in range(n):
                    graph[i][i]=a[i]
                    graph[n-i-1][i]=b[i]
                    graph[n//2][i]=c[i]
                    graph[n-i-1][n//2]=d[i] 
            else:# 오른쪽으로 회전
                for i in range(n):
                    graph[i][n-i-1]=a[i]
                    graph[i][i]=b[i]
                    graph[i][n//2]=c[i]
                    graph[n//2][i]=d[i]
    #결과 출력
    for i in range(n):
        print(*graph[i],sep=' ')