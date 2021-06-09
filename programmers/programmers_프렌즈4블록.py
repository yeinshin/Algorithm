#https://programmers.co.kr/learn/courses/30/lessons/17679
#프로그래머스-프렌즈4블록

#라이언(R), 무지(M), 어피치(A), 프로도(F), 네오(N), 튜브(T), 제이지(J), 콘(C)을 의미
#m*n
from copy import deepcopy

def solution(m, n, board):
    now = 0
    board = list(map(list,board))
    
    while True:
        answer=set()
        #2x2대로 검사하여 좌표값 저장하기 -> set으로 저장하여 중복을 제거
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j]==board[i+1][j]==board[i+1][j+1]==board[i][j+1]!='X':
                    answer.add((i,j))
                    answer.add((i+1,j))
                    answer.add((i+1,j+1))
                    answer.add((i,j+1))
        
        #지워진것이 없으면 당장 break           
        if len(answer)==0:
            break
        else:
            now +=len(answer)

        #밑으로 떨어지게 만들기
        for x,y in answer:
            board[x][y]='X'
            
        for x,y in sorted(answer):
            for i in range(0,x):
                board[x][y],board[i][y]=board[i][y],board[x][y]
    
    return now