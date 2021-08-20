#https://programmers.co.kr/learn/courses/30/lessons/17687
#프로그래머스-n진수 게임

# 2진수: bin, 16진수: hex
# n: 진법, t: 미리 구할 숫자의 개수, m: 게임에 참가하는 인원, p: 튜브의 순서
def convert(n, base):
        arr = "0123456789ABCDEF"
        q, r = divmod(n, base)
        if q == 0:
            return arr[r]
        else:
            return convert(q, base) + arr[r]

def solution(n, t, m, p):
    answer = ''
    person = [[] for _ in range(m)]
    gamenum = 0
    idx = 0

    while len(person[p-1])<t:
        for i in convert(gamenum,n):
            person[idx].append(i)
            idx+=1
            if idx==m:
                idx = 0 
        gamenum+=1
        
        if len(person[p-1])==t:
            break
        
    return (''.join(person[p-1][:t])).upper()