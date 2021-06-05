#https://www.acmicpc.net/problem/10709
#10709번-기상캐스터

h,w = map(int,input().split())

sky = [[i for i in input()] for _ in range(h)]
cloud = [(i,j) for i in range(h) for j in range(w) if sky[i][j]=='c']

for c in cloud:
    sky[c[0]][c[1]]=0
    x,y=c[0],c[1]
    cnt=0
    for _ in range(w-1):
        ny = y+1
        if 0<=ny<w and sky[x][ny]=='.':
            cnt+=1
            sky[x][ny]=cnt
            y=ny
            continue
        break

for i in range(h):
    for j in range(w):
        if sky[i][j]=='.':
            print('-1',end=' ')
        else: print(sky[i][j],end=' ')
        
    print()