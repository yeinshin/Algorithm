# https://programmers.co.kr/learn/courses/30/lessons/12922
#프로그래머스-수박수박수박수박수박수?

def solution(n):
    answer = ''
    for i in range(1,n+1):
        answer+=('수' if i%2!=0 else '박')
    return answer