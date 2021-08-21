#https://programmers.co.kr/learn/courses/30/lessons/81301
#프로그래머스-숫자 문자열과 영단어

def solution(s):
    answer = []
    words = {
        'zero':'0',
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9'
    }
    
    cnt = 0
    
    for i in range(len(s)):
        if s[i].isalpha():
            cnt+=1
            if cnt>=3 and s[i-cnt+1:i+1] in words:
                answer.append(words[s[i-cnt+1:i+1]])
                cnt = 0
        else:
            answer.append(s[i])
            cnt = 0
    
    return int(''.join(answer))

    
    # 또 다른 풀이

    def solution(s):
        words = {
            'zero':'0',
            'one':'1',
            'two':'2',
            'three':'3',
            'four':'4',
            'five':'5',
            'six':'6',
            'seven':'7',
            'eight':'8',
            'nine':'9'
        }
        
        for word in words.items():
            s=s.replace(word[0],word[1])
        
        return int(s)