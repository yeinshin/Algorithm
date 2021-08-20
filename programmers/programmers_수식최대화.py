#프로그래머스-수식 최대화

from itertools import permutations
import re

def solution(expression):
    answer = 0
    operators = list() #연산자 집합
    #숫자 리스트
    numbers = list(map(int,re.findall('\d+',expression)))
    
    for ex in expression:
        if not ex.isdigit():
            operators.append(ex)
            
    #연산자 우선순위 구하기 (순열 이용)
    permu = list(permutations(set(operators)))
    
    for p in permu:
        num = numbers[:]
        oper = operators[:]
        for i in p:
            idx = 0
            while idx<len(oper):
                if oper[idx]==i and i=='+':
                    num[idx] = num[idx]+num[idx+1]
                    del num[idx+1]
                    del oper[idx]
                    idx-=1
                elif oper[idx]==i and i=='-':
                    num[idx] = num[idx]-num[idx+1]
                    del num[idx+1]
                    del oper[idx]
                    idx-=1
                elif oper[idx]==i and i=='*':
                    num[idx] = num[idx]*num[idx+1]
                    del num[idx+1]
                    del oper[idx]    
                    idx-=1
                idx+=1
        answer = max(answer,abs(num[0]))
    
    return answer

