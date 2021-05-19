#가로길이 >= 세로길이
#[가로길이, 세로길이]

def solution(brown, yellow):
    answer = []

    for i in range(1,yellow+1):
        if yellow % i==0:
            height = i #세로길이
            width = yellow // i #가로길이

            if ((height*2) + (width*2) + 4 )==brown:
                answer.append(width+2)
                answer.append(height+2)

                break
            
    return answer