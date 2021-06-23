#https://programmers.co.kr/learn/courses/30/lessons/12913
#프로그래머스-땅따먹기

def solution(land):
    for i in range(1,len(land)):
        for j in range(len(land[0])):
            value = 0
            for k in range(len(land[0])):
                if j!=k:
                    value = max(value,land[i-1][k])       
            land[i][j] = value+land[i][j]
    
    return max(land[len(land)-1])

#-----------------------------------------------------------------#
#다른 풀이
def solution(land):
    for i in range(1,len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i-1][:j]+land[i-1][j+1:])+land[i][j]
    
    return max(land[len(land)-1])