#https://programmers.co.kr/learn/courses/30/lessons/12947
#프로그래머스-하샤드 수
def solution(x):
    total = 0
    for i in str(x):
        total+=int(i)
    return True if not x%total else False