#https://www.acmicpc.net/problem/16926
#16926번-배열 돌리기1
n,m,r = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
while cnt<=r:
    cnt+=1
    if n>=3 and m>=3:
        for x,y in ((0,0),(1,1)):
            