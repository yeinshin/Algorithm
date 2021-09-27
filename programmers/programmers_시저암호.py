#https://programmers.co.kr/learn/courses/30/lessons/12926
#프로그래머스-시저 암호
def solution(s, n):
    answer = ''
    for i in s:
        i=ord(i)
        if 65<=i<=90 and i+n>90:answer+=chr(64+(i+n)-90)
        elif 97<=i<=122 and i+n>122:answer+=chr(96+(i+n)-122)
        elif i!=32 : answer+=chr(i+n)
        else: answer+=' '
    return answer