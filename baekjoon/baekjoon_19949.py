#https://www.acmicpc.net/problem/19949
#19949번-영재의 시험
answer = list(map(int,input().split()))
result = 0
def back(cnt,before):
    global result
    if cnt == 10:
        score = 0
        for j in range(10):
            if answer[j]==before[j]:score+=1
        if score>=5: result+=1
        return
    for i in range(1,6):
        if cnt>=2 and before[-1]==before[-2]==i:
            continue
        back(cnt+1,before+[i])
back(0,[])
print(result)