#https://programmers.co.kr/learn/courses/30/lessons/12952
#프로그래머스-N-Queen

answer = 0

def dfs(column,d1,d2,n,x):
    global answer
    
    if x==n:
        answer+=1
        return
    
    for y in range(n):
        if y not in column and (x-y) not in d1 and (x+y) not in d2:
            column.append(y)
            d1.append(x-y)
            d2.append(x+y)
            dfs(column,d1,d2,n,x+1)
            column.pop()
            d1.pop()
            d2.pop()

def solution(n):
    global answer
    
    column,d1,d2=list(),list(),list()
    
    dfs(column,d1,d2,n,0)
    
    return answer