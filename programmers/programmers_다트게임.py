#https://programmers.co.kr/learn/courses/30/lessons/17682
#프로그래머스-다트 게임

def solution(dartResult):
    answer = []
    num = ''
    calc = 0
    
    for i in range(len(dartResult)):
        if dartResult[i].isdigit() :
            num+=dartResult[i]
            
        elif dartResult[i].isalpha():
            if dartResult[i] == 'S':
                calc = int(num)           
            if dartResult[i] == 'D':
                calc = int(num)**2
            if dartResult[i] == 'T':
                calc = int(num)**3
            if (i<len(dartResult)-1 and dartResult[i+1].isdigit()) or i==len(dartResult)-1 :
                # answer+=calc
                answer.append(calc)
            num=''
            
        elif dartResult[i]=='*':
            if i==2: calc*=2
            else: 
                calc*=2
                answer[-1]*=2
            if (i<len(dartResult)-1 and dartResult[i+1].isdigit()) or i==len(dartResult)-1:
                answer.append(calc)
                calc = 0
                
        elif dartResult[i] =='#':
            calc*=(-1)
            if (i<len(dartResult)-1 and dartResult[i+1].isdigit()) or i==len(dartResult)-1:
                answer.append(calc)
                calc = 0
    
    return sum(answer)