#https://programmers.co.kr/learn/courses/30/lessons/12932
#프로그래머스-자연수 뒤집어 배열로 만들기
def solution(n):
    return list(map(int,reversed(str(n))))