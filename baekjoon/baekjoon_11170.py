#https://www.acmicpc.net/problem/11170
#11170번-0의 개수

for _ in range(int(input())):
    n,m = map(int,input().split())
    result = 0
    for i in range(n,m+1):
        result += str(i).count('0')
    print(result)
    