#https://programmers.co.kr/learn/courses/30/lessons/42883
#프로그래머스-큰 수 만들기
def solution(number, k):
    number = list(map(int,number))
    answer = [number[0]]
    for n in number[1:]:
        while answer and answer[-1]<n and k>0:
            k-=1
            answer.pop()
        answer.append(n)
    if k!=0: answer=answer[:-k]
    return ''.join(map(str,answer))