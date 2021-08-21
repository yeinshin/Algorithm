#https://programmers.co.kr/learn/courses/30/lessons/67256
#프로그래머스-키패드 누르기

def solution(numbers, hand):
    answer = ''
    keypad = {
        1:[0,0],
        2:[0,1],
        3:[0,2],
        4:[1,0],
        5:[1,1],
        6:[1,2],
        7:[2,0],
        8:[2,1],
        9:[2,2],
        0:[3,1]
    }
    hand_l = [3,0]
    hand_r = [3,2]
    
    for number in numbers:
        if number in (1,4,7):
            answer+='L'
            hand_l=keypad[number]
            
        elif number in (3,6,9):
            answer+='R'
            hand_r=keypad[number]
            
        elif number in (2,5,8,0):
            left = abs(hand_l[0]-keypad[number][0]) + abs(hand_l[1]-keypad[number][1])
            right = abs(hand_r[0]-keypad[number][0]) + abs(hand_r[1]-keypad[number][1])
            
            if left<right or (left==right and hand=='left'): 
                answer+='L'
                hand_l =keypad[number]
                
            elif left>right or (left==right and hand=='right'): 
                answer+='R'
                hand_r=keypad[number]

    return answer