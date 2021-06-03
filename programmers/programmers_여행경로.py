#https://programmers.co.kr/learn/courses/30/lessons/43164
#프로그래머스-여행경로

from copy import deepcopy
answer = []

def dfs(tickets,check,n,start,visited):
    global answer

    if check.count(False)==0:    
        if len(answer)==0:
            answer = deepcopy(visited)
        return 

    for j in range(n):
        if start==tickets[j][0] and not check[j]:
            check[j]=True
            visited.append(tickets[j][1])
            dfs(tickets,check,n,tickets[j][1],visited)
            check[j]=False
            visited.pop()

def solution(tickets):
    global answer

    n = len(tickets)

    tickets.sort(key=lambda x:(x[0],x[1]))

    for i in range(n):
        check = [False]*n
        visited = list()
        if tickets[i][0]=="ICN":
            #tickets[i][1] : 목적지
            check[i]=True
            visited.append(tickets[i][0])
            visited.append(tickets[i][1])

            if len(answer)==0:
                dfs(tickets,check,n,tickets[i][1],visited)
            else:
                break
    return answer