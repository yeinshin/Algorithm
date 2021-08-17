#프로그래머스-거리두기 확인하기

#응시자 : P, 빈 테이블 : O , 파티션 : X
def solution(places):
    answer = []
    
    def find(room):
        for x in range(5):
            for y in range(5):
                if room[x][y] == 'P':
                    if x+1<5 : #↓
                        if room[x+1][y]=='P':
                            return 0
                        if x+2<5 and room[x+1][y]=='O' and room[x+2][y]=='P':
                            return 0
                    if y+1<5: #→
                        if room[x][y+1]=='P':
                            return 0
                        if y+2<5 and room[x][y+1]=='O' and room[x][y+2]=='P':
                            return 0
                    
                    if x+1<5 and y+1<5 and room[x+1][y+1]=='P' and (room[x+1][y]=='O' or room[x][y+1]=='O'):
                        return 0
                else:
                    if x+1<5 and y+1<5 and room[x+1][y]=='P' and room[x][y+1]=='P' and (room[x][y]=='O' or room[x+1][y+1]=='O'):
                        return 0
        
        return 1
                    
    for i in range(5):
        answer.append(find(places[i]))
        
    return answer