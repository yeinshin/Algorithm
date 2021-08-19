#https://www.acmicpc.net/problem/20437
#20437번-문자열 게임 2
import sys
from collections import Counter

input = sys.stdin.readline

for _ in range(int(input())):
    w = input().rstrip()
    k = int(input())
    test = Counter(w)
    game = list()
    for i in test.items():
        if i[1]>=k:
            game.append(i[0])

    if len(game)==0:
        print(-1)
    else:
        max_d = 0
        min_d = 10000
        for g in game:
            index = list()
            for i,v in enumerate(w):
                if v==g:
                    index.append(i)
                
            for a in range(len(index)-k+1):
                max_d = max(max_d,index[a:a+k][-1]-index[a:a+k][0]+1)
                min_d = min(min_d,index[a:a+k][-1]-index[a:a+k][0]+1)

        print(min_d,max_d)
    

