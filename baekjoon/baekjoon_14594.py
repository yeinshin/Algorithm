#https://www.acmicpc.net/problem/14594
#14594번-동방 프로젝트

n = int(input())
m = int(input())
rooms = [[False]*2 for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    if a<b:
        for i in range(a-1,b-1):
            rooms[i][1]=True
            rooms[i+1][0]=True
check = False
result = 0
for i in range(n):
    if rooms[i][1] and not check:
        check=True
        result +=1
    elif check and i!=n-1 and not rooms[i][1] and not rooms[i+1][0]:
        check=False
    elif not check and not rooms[i][0] and not rooms[i][1]:
        result +=1
print(result)
