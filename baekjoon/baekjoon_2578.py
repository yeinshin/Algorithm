#https://www.acmicpc.net/problem/2578
#2578번-빙고
bingo = [list(map(int,input().split())) for _ in range(5)]
num = [list(map(int,input().split())) for _ in range(5)]
answer=0
cnt=0
def check():
    x = 0
    for i in range(5):
        if sum(bingo[i])==0:x+=1
    c = list(map(list,zip(*bingo)))
    for i in range(5):
        if sum(c[i])==0: x+=1       
    if bingo[0][0]+bingo[1][1]+bingo[2][2]+bingo[3][3]+bingo[4][4]==0:x+=1
    if bingo[0][4]+bingo[1][3]+bingo[2][2]+bingo[3][1]+bingo[4][0]==0:x+=1
    if x>=3:return True
    return False

for i in range(5):
    for j in range(5):
        for a in range(5):
            for b in range(5):
                if num[i][j]==bingo[a][b]:
                    cnt+=1
                    answer+=1
                    bingo[a][b]=0
        if cnt>=5 and check():
            print(answer)
            exit()

