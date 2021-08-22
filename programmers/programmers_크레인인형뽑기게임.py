#https://programmers.co.kr/learn/courses/30/lessons/64061
#프로그래머스-크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    basket = list()
    board = list(map(list,zip(*board)))
    
    for move in moves:
        for i in range(len(board)):
            if sum(board[move-1])==0:
                break
            if board[move-1][i]!=0 :
                if basket and basket[-1]==board[move-1][i]:
                    basket = basket[:-1]
                    answer+=2
                else: basket.append(board[move-1][i])
                    
                board[move-1][i]=0
                break
        
    return answer