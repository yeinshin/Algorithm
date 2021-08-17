#프로그래머스-튜플

from collections import defaultdict

def solution(s):
    answer = []
    a = defaultdict(int)
    s = s.split(',')
    for i in range(len(s)):
        num = ''
        for j in range(len(s[i])):
            if s[i][j].isdigit():
                num+=s[i][j]
        a[int(num)]+=1
    
    for t in sorted(list(a.items()),key = lambda x: -x[1]):
        answer.append(t[0])
        
    return answer


#[코드 리팩토링]

#Counter 함수도 items() 메서드 사용이 가능하다
#re.findall('\d+',list) -> 문자열 안에 숫자만 골라내서 리스트로 만들어줌
#Ex) "{{20,111},{111}}" -> ['20', '111', '111']

from collections import Counter
import re

def solution(s):
    s = list(map(int,re.findall('\d+',s)))   
    return [t[0] for t in sorted(list(Counter(s).items()),key=lambda x: -x[1])]