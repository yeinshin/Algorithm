#https://programmers.co.kr/learn/courses/30/lessons/12935
#프로그래머스-제일 작은 수 제거하기
def solution(arr):
    del arr[arr.index(min(arr))]    
    return arr if arr else [-1]