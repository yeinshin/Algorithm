#https://programmers.co.kr/learn/courses/30/lessons/72411
#프로그래머스-메뉴 리뉴얼
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order), c)
            temp += combi
        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)