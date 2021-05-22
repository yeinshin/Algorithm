#15683번-감시/다시 풀어보기 .... 재귀... 어렵다.. ㅜ
#1번 CCTV는 한 쪽 방향만 감시할 수 있다. 2번과 3번은 두 방향을 감시할 수 있는데, 2번은 감시하는 방향이 서로 반대방향이어야 하고, 3번은 직각 방향이어야 한다. 4번은 세 방향, 5번은 네 방향을 감시할 수 있다.
from copy import deepcopy
import sys

input = sys.stdin.readline

def fill(x, y, arr, d):

    #방향의 개수만큼 for문 반복
    #1번 방향: 1개, 2번 방향: 2개, 3번 방향: 2개, 4번 방향: 3개, 5번 방향: 4개
    for i in d:
        nx, ny = x, y

        #벽을 만날때까지 지정된 방향으로 직진!
        while True:
            #현재 좌표값에서 이동했을 때의 좌표값
            nx += dx[i]
            ny += dy[i]

            #좌표값이 n,m 범위에서 벗어나지 않는다면,
            if 0 <= nx < n and 0 <= ny < m:

                #벽을 만났을 때는 break (while문 탈출)
                if arr[nx][ny] == 6:
                    break

                #cctv 범위를 '#'로 변경 해준다
                elif arr[nx][ny] == 0:
                    arr[nx][ny] = "#"
            
            #좌표값 n,m 범위에서 벗어나면 즉시 break
            else:
                break


def dfs(arr, cnt):

    global result

    #맨처음 함수가 실행될 때, 리스트 temp는 선언된 s 리스트를 deepcopy 한다.
    temp = deepcopy(arr)

    if cnt == cctv_cnt:
        num = 0
        #cctv가 설치된 리스트 temp의 0의 갯수를 count 해줌
        for i in range(n):
            num += temp[i].count(0)
        result = min(result, num)
        print('cnt:',cnt,'재귀 종료')
        return

    x, y, cctv = q[cnt]

    for i in direction[cctv]:
        print('i:',i,end='\n\n')
        print('x:',x,'y:',y,'cctv:',cctv,end='\n\n')
        print('함수 fill 실행 전:',*temp,sep='\n',end='\n\n')

        #cctv의 x,y 좌표값과 방향값을 함수 fill에 넘겨준다 
        fill(x, y, temp, i) # 함수 실행 후 -> temp에 설치가 되어있다.

        print('함수 fill 실행 후:',*temp,sep='\n',end='\n\n')

        #cctv가 설치가 된 상태의 리스트와 설치한 cctv의 갯수를 넘겨줌
        dfs(temp, cnt + 1)

        #다시 시작 리스트로 deepcopy 하기 위해 선언해줌
        temp = deepcopy(arr)
        print('cnt:',cnt,end='\n\n')
        print('cctv',cctv,'번이','deepcopy가 되었습니다!')
        print(*temp,sep='\n',end='\n\n')


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
direction = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[3, 0], [0, 2], [2, 1], [1, 3]], 
[[1, 3, 0], [3, 0, 2], [0, 2, 1], [2, 1, 3]], [[0, 1, 2, 3]]]
n, m = map(int, input().split())
s = []
q = []
cctv_cnt = 0
result = 100000000

for i in range(n):
    a = list(map(int, input().split()))
    s.append(a)
    for j in range(len(a)):
        if a[j] != 0 and a[j] != 6:

            #x(cctv의 x좌표값),y(cctv의 y좌표값),cctv번호
            q.append([i, j, a[j]])
            cctv_cnt += 1
dfs(s, 0)
print()
print('q:',q,end= '\n\n')
print(result)
