#https://www.acmicpc.net/problem/9095
#9095번-1,2,3 더하기/원리를 모르겠어서 풀이 참고함

d = [1,2,4] + [0]*7
for i in range(3,10):
    d[i] = d[i-1]+d[i-2]+d[i-3]
for _ in range(int(input())):
    n = int(input())
    print(d[n-1])
    