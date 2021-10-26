#https://www.acmicpc.net/problem/7568
#7568번-덩치
#자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1이 된다. 
n = int(input())
d = [list(map(int,input().split())) for _ in range(n)]
result = []
for i in range(n):
    a,b = d[i][0],d[i][1]
    k = 0
    for a1,b1 in d[:i]+d[i+1:]:
        if a1>a and b1>b:k+=1
    result.append(k+1)
print(*result,sep=' ')
