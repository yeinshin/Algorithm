#https://www.acmicpc.net/problem/20055
#20055번-컨베이어 벨트 위의 로봇

#1번 칸이 있는 위치: 올리는 위치
#N번 칸이 있는 위치를 내리는 위치
#내구도가 0인 칸의 개수가 k개 이상이라면 과정을 종료


n,k= map(int,input().split())
score = list(map(int,input().split()))
cnt = 0
box = [False]*n

while score.count(0)<k:
    cnt+=1
    #1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다. 내리는 위치에 있는 로봇은 내린다.
    score = [score[2*n-1]] + score[:2*n-1]
    box = [False] + box[:n-2] + [False]

    #2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다
       #1. 로봇이 이동하기 위해서는 로봇이 내리는 위치가 아니고, 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
    if box.count(False)!=n:
        for i in range(n-2,-1,-1):
            if box[i]: 
                if i+1!=n and not box[i+1] and score[i+1]>=1:
                    box[i]=False
                    box[i+1]=True
                    score[i+1]-=1

    #3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if score[0]!=0:
        score[0]-=1
        box[0]=True
    
    #4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.

print(cnt)