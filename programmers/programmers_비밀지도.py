#https://programmers.co.kr/learn/courses/30/lessons/17681
#프로그래머스-비밀지도

def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        answer.append(format(arr1[i] | arr2[i],'b').zfill(n).replace('1','#').replace('0',' '))
    return answer