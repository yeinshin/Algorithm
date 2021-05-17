#1018번-체스판 다시 칠하기/다시 풀어보기

#NxM
n, m = map(int, input().split())
graph = [[i for i in input()] for _ in range(n)]
mini = list()

for a in range(n - 7):
    for i in range(m - 7):
        idx1 = 0
        idx2 = 0
        for b in range(a, a + 8):
            for j in range(i, i + 8):              
                #맨왼쪽 맨 위쪽이 W 일때랑 B 일때의 경우를 한꺼번에 세어준다. -> 8X8 범위를 B와 W로 번갈아가면서 검사
                if (j + b)%2 == 0: #짝수일 때

                    #W로 시작할때의 경우 idx1 변수에 저장
                    if graph[b][j] != 'W': idx1 += 1  
                    #B로 시작할때의 경우 idx2 변수에 저장
                    if graph[b][j] != 'B': idx2 += 1

                else : #홀수일 때 , 짝수일 떄
                    #W로 시작할때의 경우 idx1 변수에 저장
                    if graph[b][j] != 'B': idx1 += 1
                    #B로 시작할때의 경우 idx2 변수에 저장
                    if graph[b][j] != 'W': idx2 += 1
        mini.append(idx1)                          # W로 시작했을 때 칠해야 할 부분
        mini.append(idx2)                          # B로 시작했을 때 칠해야 할 부분

print(min(mini))