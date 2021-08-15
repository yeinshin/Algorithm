#프로그래머스-파일명 정렬

#두 파일의 HEAD 부분과, NUMBER의 숫자도 같을 경우, 원래 입력에 주어진 순서를 유지한다.
# HEAD 부분을 기준으로 사전 순으로 정렬 -> NUMBER의 숫자 순으로 정렬

# 대소문자 구분 없이 소팅
# a.sort(key=str.lower)

def solution(files):
    answer = []
    test = []
    
    for file in files:
        char = ''
        num = 0
        start,end = 0,0
        
        for i in range(len(file)):
            if file[i].isdigit():
                start = i
                end = start
                char = file[:i]
                while True:
                    end +=1
                    if end>=len(file) or not file[end].isdigit() :
                        num = file[start:end]
                        break
                break
        test.append((char,num,file[end:]))
        
    for t in sorted(test, key = lambda x : (x[0].lower(),int(x[1]))):
        answer.append(''.join(t))
        
    return answer

solution(["img12", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])