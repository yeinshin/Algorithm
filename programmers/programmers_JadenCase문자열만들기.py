#프로그래머스-JadenCase 문자열 만들기(capitalize() 참고)

#파이썬 capitalize(); 파이썬 문자열 capitalize(). 문자열의 첫글자는 대문자로, 나머지는 소문자로 변환한다. 
def solution(s):
    change = s.split(' ')
    
    for i in range(len(change)):
        change[i] = change[i].capitalize()
        
    return ' '.join(change)  