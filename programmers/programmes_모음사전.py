#https://programmers.co.kr/learn/courses/30/lessons/84512
#프로그래머스-모음사전
from itertools import product
def solution(word):
    alphabet = ['A','E','I','O','U']
    s=[]
    for i in range(1,6):
        s.extend(list(map(''.join,product(alphabet,repeat=i))))
    return sorted(s).index(word)+1