#https://programmers.co.kr/learn/courses/30/lessons/49993
#프로그래머스-스킬트리

def solution(skill, skill_trees):
    answer = 0
    
    for s in skill_trees:
        idx = 0 
        check = 0
        for i in range(len(s)):
            if s[i] in skill:
                check +=1
            if s[i] == skill[idx]:
                idx+=1
                if (idx == len(skill)-1 or idx == len(skill)) :
                    break
        
        if (idx == 0 and check==0) or (idx>0 and idx>=check):
            answer+=1
        
    return answer