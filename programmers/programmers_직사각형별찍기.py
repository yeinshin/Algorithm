#https://programmers.co.kr/learn/courses/30/lessons/12969
#프로그래머스-직사각형 별찍기
a, b = map(int, input().split())
for i in range(b):
    for j in range(a):
        print('*',end='')
    print()