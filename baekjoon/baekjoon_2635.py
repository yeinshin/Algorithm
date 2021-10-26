#https://www.acmicpc.net/problem/2635
#2635번-수 이어가기

n = int(input())
answer = []
for i in range(n,-1,-1):
    result = [n]
    result.append(i)
    cnt = 0
    while 1:
        cnt = result[-2]-result[-1]
        if cnt>-1: result.append(cnt)
        else: break
    answer.append((len(result),result[:]))
answer.sort(key = lambda x:-x[0])
print(answer[0][0])
print(*answer[0][1],sep=' ')