#https://www.acmicpc.net/problem/10703
#10703번-유성(풀이참고)
#문자 'X'는 유성의 일부를, 문자 '#'는 땅의 일부를, 그리고 나머지는 문자'.'로 이루어져 있다
R, S = map(int, input().split())
meteor = [input() for _ in range(R)]    
arr = [['.'] * S for _ in range(R)]    
 
max_meteor = [-int(1e9)] * S    # 유성 좌표를 저장 할 리스트
min_ground = [int(1e9)] * S    # 땅 좌표를 저장 할 리스트
 
for x in range(R):
    for y in range(S):
        if meteor[x][y] == 'X':
            max_meteor[y] = max(max_meteor[y], x)    # 현재 유성의 y좌표(열)를 갱신함
        elif meteor[x][y] == '#':
            min_ground[y] = min(min_ground[y], x)    # 현재 땅의 y좌표(열)를 갱신함
 
move = min((j-i for i, j in zip(max_meteor, min_ground))) - 1    # 최종적으로 가야 할 move 계산
 
for x in range(R):
    for y in range(S):
        if meteor[x][y] == 'X': arr[x+move][y] = 'X'
        elif meteor[x][y] == '#': arr[x][y] = '#'
 
for i in range(R):    # 결과 출력
    print(*arr[i],sep='')