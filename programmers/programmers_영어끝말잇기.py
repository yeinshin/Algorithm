#프로그래머스-영어 끝말잇기

def solution(n, words):
    answer = []
    people =  [[] for _ in range(n)]
    word = list()
    idx = 1
    end = words[0][0]
    
    for i in range(1,len(words)+1):
        if words[i-1] not in word and end == words[i-1][0]:
            people[idx-1].append(words[i-1])
            word.append(words[i-1])
            end = words[i-1][-1]
            
            idx +=1 
            if idx >n:
                idx = 1
            
        else: return [idx,len(people[idx-1])+1]
        
    return [0,0]