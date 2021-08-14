#프로그래머스-방금그곡

#네오가 기억한 멜로디와 악보에 사용되는 음은 C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개이다.
#조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 
#재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
#음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보가 ','로 구분된 문자열이다.

def solution(m, musicinfos):
    
    m = m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    
    playlist = list()
    index = 0
    
    for music in musicinfos:
        
        index+=1
        
        #방송된 곡의 정보
        info = music.split(',')
        
        #재생시간
        play = (int(info[1].split(':')[0])*60+int(info[1].split(':')[1]))-(int(info[0].split(':')[0])*60+int(info[0].split(':')[1]))
        
        #음악 이름
        name = info[2]

        music = info[3].replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
        if m in music*(play//len(music)) + music[:play%len(music)]:
            playlist.append((play,index,name))
    
    
    if not len(playlist):
        return "(None)"
    elif len(playlist)==1:
        return playlist[0][2]
    else:
        playlist = sorted(playlist,key = lambda x : (-x[0],x[1]))
        return playlist[0][2]
    