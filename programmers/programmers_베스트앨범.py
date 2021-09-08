#https://programmers.co.kr/learn/courses/30/lessons/42579#
#프로그래머스-베스트앨범

from collections import defaultdict
def solution(genres, plays):
    answer = []
    play = defaultdict(list)
    n = len(genres)
    for i in range(n):
        play[genres[i]].append(plays[i])
            
    play = sorted(play.items(),key = lambda x : -sum(x[1]))
    for i in range(len(play)):
        p =sorted(play[i][1],reverse = True)
        if len(p)==1:
            answer.append(plays.index(p[0]))
        else:
            for a in range(2):
                for j in range(n):
                    if play[i][0]==genres[j] and plays[j]==p[a] and j not in answer:
                        answer.append(j)
                        break
                        
    return answer