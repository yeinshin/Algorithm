#https://www.acmicpc.net/problem/20053
#20053번-최소, 최대2
for _ in range(int(input())):
    n = int(input())
    num = list(map(int,input().split()))
    print(min(num),max(num))