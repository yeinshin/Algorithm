#https://www.acmicpc.net/problem/18808
#18808번-스티커 붙이기
n,m,k = map(int,input().split())
notebook = [[0]*m for _ in range(n)]

def fit(x,y,r,c): #정확하게 맞아 들어가는지 확인
    if r>n or c>m: return False
    for i in range(r):
        for j in range(c):
            if sticker[i][j]+notebook[i+x][j+y]==2: return False
    return True

def store(x,y,r,c): #notebook에 sticket 붙여주기
    for i in range(r):
        for j in range(c):
            if sticker[i][j]==1: notebook[i+x][j+y]=1

for _ in range(k):
    r,c = map(int,input().split())
    sticker = [list(map(int,input().split())) for _ in range(r)]
    check = False
    for i in range(n-r+1):
        for j in range(m-c+1):
            if fit(i,j,r,c):
                store(i,j,r,c)
                check = True
                break
        if check: break
    if check:continue

    cnt = 1
    while cnt<=3:
        sticker=[k[::-1] for k in zip(*sticker)]
        r,c = len(sticker),len(sticker[0])
        for i in range(n-r+1):
            for j in range(m-c+1):
                if fit(i,j,r,c):
                    store(i,j,r,c)
                    check = True
                    break
            if check: break
        if check: break
        else: cnt+=1
result = 0
for i in range(n):
    result +=sum(notebook[i])
print(result)