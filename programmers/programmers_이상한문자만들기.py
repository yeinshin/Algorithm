#https://programmers.co.kr/learn/courses/30/lessons/12930
#프로그래머스-이상한 문자 만들기
def solution(s):
    answer = list()
    for i in s.split(' '):
        c = ''
        for j in range(len(i)):
            if j%2==0:c+=i[j].upper()
            else: c+=i[j].lower()
        answer.append(c)
    return ' '.join(answer)