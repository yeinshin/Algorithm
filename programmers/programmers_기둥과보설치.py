#https://programmers.co.kr/learn/courses/30/lessons/60061
#프로그래머스-기둥과 보 설치

#a-> 0:기둥, 1:보
#b-> 0:삭제, 1:설치
def check (answer):
    for b in answer:
        if b[2]==0:#기둥일때
                # 기둥이 바닥 위에 있거나/ 보의 한쪽 끝부분 위에 있거나/ 다른 기둥 위에 있어야 합니다.
                if b[1]==0 or [b[0]-1,b[1],1] in answer or [b[0],b[1],1] in answer or [b[0],b[1]-1,0] in answer:
                    continue
                return False
                    
        if b[2]==1:#보일때
            #한쪽 끝부분이 기둥 위에 있거나/ 양쪽 끝부분이 다른 보와 동시에 연결되어 있어야 합니다.
            if ([b[0]+1,b[1]-1,0] in answer or [b[0],b[1]-1,0] in answer) or ([b[0]-1,b[1],1] in answer and [b[0]+1,b[1],1] in answer):
                continue
            return False
    
    return True
    
def solution(n, build_frame):
    answer = []
    
    for b in build_frame:
        
        if b[3]==1:#설치
            answer.append([b[0],b[1],b[2]])
            if not check(answer):
                answer.remove([b[0],b[1],b[2]])
        
        if b[3]==0:#삭제
            answer.remove([b[0],b[1],b[2]])
            if not check(answer):
                answer.append([b[0],b[1],b[2]])
                
    return sorted(answer,key=lambda x: (x[0],x[1],x[2])) #sorted(answer)로 해도 됨