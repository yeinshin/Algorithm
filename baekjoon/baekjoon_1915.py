#https://www.acmicpc.net/problem/1915
#1915번-가장 큰 정사각형
def solution(board):
    answer = 0
    
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j]!=0 and board[i-1][j]!=0 and board[i-1][j-1]!=0 and board[i][j-1]!=0:
                board[i][j] = min(board[i-1][j],board[i-1][j-1],board[i][j-1])+1

    for i in range(len(board)):
        answer = max(answer,max(board[i]))
                
    
    return answer**2

n,m = map(int,input().split())
graph = [[int(m) for m in input()] for _ in range(n)]

print(solution(graph))