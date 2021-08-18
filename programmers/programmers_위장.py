#프로그래머스-위장(경우의 수 풀이 방법 참고)
from collections import defaultdict

def solution(clothes):
    answer = 1
    category = defaultdict(int)
    
    for a,b in clothes:
        category[b]+=1
    
    for i in list(category.values()):
        answer = answer*(i+1)
    
    
    return answer-1