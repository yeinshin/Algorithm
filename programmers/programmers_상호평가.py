#프로그래머스-상호 평가(위클리 챌린지)
answer = ''

def grade(score):
    global answer    
    
    if score>=90:
        answer+='A'
    elif 80<=score<90:
        answer+='B'
    elif 70<=score<80:
        answer+='C'
    elif 50<=score<70:
        answer+='D'
    else: answer+='F'
    
def solution(scores):
    global answer
    avg = 0
    
    for j in range(len(scores)):
        lst = list()
        for i in range(len(scores)):
            lst+=[scores[i][j]]
        
        if (max(lst)==scores[j][j] or min(lst)==scores[j][j] ) and lst.count(scores[j][j])==1:
            avg = sum(lst[0:j]+lst[j+1:])/(len(scores)-1)
        else:
            avg = sum(lst)/len(scores)
        grade(avg)

    return answer

#열 중심으로 만들기
#scores = list(map(list, zip(*scores)))