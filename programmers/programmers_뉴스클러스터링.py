#프로그래머스-뉴스 클러스터링 (Counter 사용법 참고함)
#다중 집합은 Counter 클래스를 이용하자 !

from collections import Counter

def twoslicing (s):
    record = list()
    
    for i in range(len(s)-1):
        if s[i].isalpha() and s[i+1].isalpha():
            record.append(s[i]+s[i+1])
            
    return record
                    
def solution(str1, str2):
    answer = 0
    
    str1 = twoslicing(str1.lower())
    str2 = twoslicing(str2.lower())
    
    inter = list((Counter(str1) & Counter(str2)).elements())
    union = list((Counter(str1) | Counter(str2)).elements())
    
    if len(inter) == 0 and len(union) == 0:
        return 65536
    else:
        return int((len(inter)/len(union))*65536)
    