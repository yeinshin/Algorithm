#프로그래머스-방문 길이

def solution(dirs):
    answer = 0
    locations = list()
    x,y = 0,0
    
    for direc in dirs:
        
        if direc == 'U'and y+1 <= 5 :
            if (x,y,x,y+1) not in locations and (x,y+1,x,y) not in locations:
                answer +=1
                locations.append((x,y,x,y+1))
            y+=1
            
        elif direc == 'D' and y-1 >= -5 :
            if (x,y,x,y-1) not in locations and (x,y-1,x,y) not in locations:
                answer+=1
                locations.append((x,y,x,y-1))
            y-=1
            
        elif direc == 'R' and x+1 <=5 :
            if (x,y,x+1,y) not in locations and (x+1,y,x,y) not in locations:
                answer+=1
                locations.append((x,y,x+1,y))
            x+=1
            
        elif direc == 'L' and x-1 >= -5 :
            if (x,y,x-1,y) not in locations and (x-1,y,x,y) not in locations:
                answer+=1
                locations.append((x,y,x-1,y))
            x-=1
        
    return answer