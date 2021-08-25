#https://programmers.co.kr/learn/courses/30/lessons/84325
#프로그래머스-직업군 추천하기(위클리 챌린지)

def solution(table, languages, preference):
    answer = list()

    for t in table:
        l = t.split()
        score = 0
        for i in range(len(languages)):
            for j in range(len(l)):
                if languages[i] == l[j]:
                    score+=(6-j)*preference[i]
                    break
        answer.append((score,l[0]))
        
    return sorted(answer,key = lambda x: (-x[0],x[1]))[0][1]