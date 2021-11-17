#https://www.acmicpc.net/problem/9207
#9207번-페그 솔리테어
from collections import deque
t = int(input())
for i in range(t):
    board = [list(input()) for _ in range(5)]
    if i!=t-1: s=input()
    pin = []
    ans = []
    for i in range(5):
        for j in range(9):
            if board[i][j]=='o':pin.append((i,j))
    
    for a,b in pin:
        print('pin a:',a,'pin b:',b)
        q = deque([(a,b,0)])
        visited = [[0]*9 for _ in range(5)]
        visited[a][b]=1
        check = 0
        while q:
            x,y,cnt = q.popleft()
            print('x:',x,'y:',y,'cnt:',cnt)
            check = max(check,cnt)
            if 0<=x+2<5 and not visited[x+1][y] and not visited[x+2][y] and board[x+1][y]=='o' and board[x+2][y]=='.':
                visited[x+1][y]=1
                visited[x+2][y]=1
                q.append((x+2,y,cnt+1))
            if 0<=x-2<5 and not visited[x-1][y] and not visited[x-2][y] and board[x-1][y]=='o' and board[x-2][y]=='.':
                visited[x-1][y]=1
                visited[x-2][y]=1
                q.append((x-2,y,cnt+1))
            if 0<=y+2<9 and not visited[x][y+1] and not visited[x][y+2] and board[x][y+1]=='o' and board[x][y+2]=='.':
                visited[x][y+1]=1
                visited[x][y+2]=1
                q.append((x,y+2,cnt+1))
            if 0<=y-2<9 and not visited[x][y-1] and not visited[x][y-2] and board[x][y-1]=='o' and board[x][y-2]=='.':
                visited[x][y-1]=1
                visited[x][y-2]=1
                q.append((x,y-2,cnt+1))
        ans.append((check,len(pin)-check))
    print(ans)