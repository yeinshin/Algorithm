#https://programmers.co.kr/learn/courses/30/lessons/72410
#프로그래머스-신규 아이디 추천

#아이디의 길이는 3자 이상 15자 이하여야 한다.
#아이디는 알파벳 소문자, 숫자, - , _ , . 문자만 사용할 수 있다.
#단, 마침표 . 는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없다. 

def solution(new_id):
    answer = ''
    test = list() #2단계를 수행한 문자를 저장할 리스트
    
    #1단계 new_id의 모든 대문자를 대응되는 소문자로 치환한다.
    new_id = new_id.lower()
    
    #2단계 new_id에서 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표를 제외한 모든 문자를 제거
    for id in new_id:
        if id.isalnum() or id in ('-','_','.') :
            test.append(id)
    
    #3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표로 치환
    change = list()
    check_dot = False
    for i in range(len(test)):
        if test[i]=='.':
            check_dot = True
        else:
            if check_dot:
                change.append('.')
                check_dot = False
            change.append(test[i])
    
    
    #4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거
    if change and change[0]=='.': change.pop(0)
    if change and change[-1]=='.': change.pop()
    
    #5단계 new_id가 빈 문자열 이라면, new_id에 'a'를 대입
    if not change: 
        change.append('a')
    
    #6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자만 저장
    #만약에 제거 후에 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표 문자 제거
    if len(change)>=16: 
        change = change[:15]
        if change[-1]=='.': change.pop()
    
    #7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙인다. 
    if len(change)<=2:
        while len(change)!=3:
            change.append(change[-1]) #change+=change[-1]도 가능함
                
    return ''.join(change)