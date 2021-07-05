#https://programmers.co.kr/learn/courses/30/lessons/12904
#프로그래머스-가장 긴 팰린드롬

def search(left,right,s):
    
    while left>=0 and right<len(s) and s[left] == s[right]:
        left-=1
        right+=1
        
    return len(s[left+1:right])
        

def solution(s):
    answer = 0
    
    if len(s)<2 or s==s[::-1]:
        return len(s)
    
    for i in range(len(s)-1):
        answer = max(answer,search(i,i+1,s),search(i,i+2,s))
    
    return answer

print(solution("abacde"))
