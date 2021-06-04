#2부<문제>2번-왕실의 나이트

#8x8
now = list(input())
dx = [-2,-2,2,2,-1,-1,1,1]
dy = [-1,1,-1,1,2,-2,2,-2]
result = 0

for i in range(8):
    nx = (int(now[1])-1) + dx[i]
    ny = (ord(now[0])-97) + dy[i]
    if 0<=nx<8 and 0<=ny<8:
        result+=1

print(result)
