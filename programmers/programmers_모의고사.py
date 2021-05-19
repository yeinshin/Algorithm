#프로그래머스-모의고사

#[cycle]
# >>> emp_pool = itertools.cycle(['김은경', '이명자', '이성진'])
# >>> next(emp_pool)
# '김은경'
# >>> next(emp_pool)
# '이명자'
# >>> next(emp_pool)
# '이성진'
# >>> next(emp_pool)
# '김은경'
# >>> next(emp_pool)
# '이명자'

def solution(answers):
    answer = []
    
    person1 = [1,2,3,4,5]
    person2 = [2,1,2,3,2,4,2,5]
    person3 = [3,3,1,1,2,2,4,4,5,5]
    
    result = [0]*3
    
    for a in range(len(answers)):
        if answers[a]==person1[a%len(person1)]:
            result[0] +=1
        if answers[a]==person2[a%len(person2)]:
            result[1] +=1
        if answers[a]==person3[a%len(person3)]:
            result[2] +=1
    
    for index,value in enumerate(result):
        print('index:',index,'value:',value)
        if value == max(result):
            answer.append(index+1)

    
    return answer