#https://www.acmicpc.net/problem/2239
#2239번-스도쿠/다시 풀어보기

import sys

sdk = [list(map(int, input())) for _ in range(9)]

#value가 0인 x와 y좌표를 리스트에 저장
# for i in range(9):
#     for j in range(9):
#         if sdk[i][j]==0:
#             zeros.append((i,j))
zeros = [(i, j) for i in range(9) for j in range(9) if sdk[i][j] == 0]


def sdoku(index):

    # 한 바퀴에서 모든 경우를 다 보았으면 출력
    # len(zeros): 스도쿠의 빈칸의 수
    # index+1을 통해 스도쿠의 빈칸의 수만큼 채웠으면 return해라
    if index == len(zeros):
        for row in sdk:
            print(*row,sep='')
        sys.exit(0)

    else:
        #zero: 스도쿠의 빈칸의 좌표를 저장해 놓은 리스트
        #zero[index][0]:빈칸의 x좌표, zero[index][1]:빈칸의 y좌표
        x = zeros[index][0]
        y = zeros[index][1]

        #빈칸의 좌표를 3으로 나눈 목에서 3을 곱하면 빈칸의 3x3 box 구역을 알 수 있다
        dx = (x//3) * 3
        dy = (y//3) * 3


        #[가로,세로,박스를 검사해서 사용하지 못하는 숫자들을 찾는 작업]
        #------------------------------------------------------------------------------------------#
        # 사용할 수 있는 숫자 9개 
        # num_list[0]=False
        # num_list[1:10]=True (1~9까지의 숫자)
        # 숫자를 인덱스로 이용
        #num_list = [True]*10
        #num_list[0] = False
        num_list = [False] + [True for _ in range(9)]

        for j in range(9):
            # 행 검사 (가로 검사)
            # sdk[x][j]가 0이 아닌 (=빈칸이 아닌) 값이 나오면 False로 바꿔라 (그 숫자는 사용 못한다)
            if(sdk[x][j]):
                num_list[sdk[x][j]] = False       
            
            # 열 검사 (세로 검사)
            if(sdk[j][y]):
                num_list[sdk[j][y]] = False

        # 3*3 box 검사
        for i in range(dx, dx + 3):
            for j in range(dy, dy + 3):
                check_num = sdk[i][j]
                #빈칸이 아닌 칸의 숫자들도 사용 못하도록 False로 바꿈
                if(check_num):
                    num_list[check_num] = False
        #------------------------------------------------------------------------------------------#

        # 현재 가능한 수만 가져옴
        # 가능한 수를 가져왔으면, 이전에 다뤄왔던 백트래킹을 사용하면 됨
        # 사용가능한 숫자이면 candidate_list에 저장해라
        # i:인덱스번호, k:False(사용x) or True(사용o)
        # for i,k in enumerate(num_list):
        #     if k:
        #         candidate_list.append(i)
        candidate_list = [i for i, k in enumerate(num_list) if k]
        
        # 경우의 수 고려
        # x = zeros[index][0]
        # y = zeros[index][1]
        for num in candidate_list:
            sdk[x][y] = num
            sdoku(index + 1)
            sdk[x][y] = 0

sdoku(0)