#https://programmers.co.kr/learn/courses/30/lessons/43165
#프로그래머스-타겟 넘버
answer = 0
def dfs(result,cnt,numbers,target):
    global answer
    
    if cnt==len(numbers):
        if result==target: 
            answer+=1
        return
    
    for j in (-numbers[cnt],+numbers[cnt]):
        dfs(result+j,cnt+1,numbers,target)
            
def solution(numbers, target):
    global answer
    dfs(0,0,numbers,target)
    return answer