# https://www.acmicpc.net/problem/14891
# 14891번-톱니바퀴

t = [list(input()) for _ in range(4)]
state = [0]*3


def check():
    state[0] = 1 if t[0][2] == t[1][6] else 0
    state[1] = 1 if t[1][2] == t[2][6] else 0
    state[2] = 1 if t[2][2] == t[3][6] else 0


def spin(i):
    global d
    if d == -1:
        t[i] = t[i][1:] + [t[i][0]]
    else:
        t[i] = [t[i][-1]] + t[i][:-1]


for _ in range(int(input())):
    idx, d = map(int, input().split())
    check()
    spin(idx-1)
    d = 1 if d == -1 else -1

    if idx == 1:
        if state[0] == 0:
            spin(1)
            d = 1 if d == -1 else -1
            if state[1] == 0:
                spin(2)
                d = 1 if d == -1 else -1
                if state[2] == 0:
                    spin(3)
                    d = 1 if d == -1 else -1
    elif idx == 2:
        if state[0] == 0:
            spin(0)
        if state[1] == 0:
            spin(2)
            d = 1 if d == -1 else -1
            if state[2] == 0:
                spin(3)
    elif idx == 3:
        if state[2] == 0:
            spin(3)
        if state[1] == 0:
            spin(1)
            d = 1 if d == -1 else -1
            if state[0] == 0:
                spin(0)
    else:
        if state[2] == 0:
            spin(2)
            d = 1 if d == -1 else -1
            if state[1] == 0:
                spin(1)
                d = 1 if d == -1 else -1
                if state[0] == 0:
                    spin(0)
ans, score = 0, 1
for i in range(4):
    if int(t[i][0]) == 1:
        ans += score
    score *= 2
print(ans)
