#https://programmers.co.kr/learn/courses/30/lessons/12910
#프로그래머스-나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    answer = []
    for a in arr:
        if a%divisor==0: answer.append(a)
    return sorted(answer) if answer else [-1]