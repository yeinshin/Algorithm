#https://www.acmicpc.net/problem/1059
#1059번-좋은 구간
#A와 B는 양의 정수이고, A < B를 만족한다.
#A ≤ x ≤ B를 만족하는 모든 정수 x가 집합 S에 속하지 않는다.
#n을 포함하는 좋은 구간의 개수를 구해보자 
L = int(input())
s = list(map(int,input().split()))
n = int(input())
if n in s: print(0)
else:
    start = 1
    end = 1001
    for i in s:
        if i<n: start=max(start,i+1)
        elif i>n: end=min(end,i)
    result = 0
    for i in range(start,n+1):
        k= n if i+1<n else i+1
        for j in range(k,end):
            result +=1
    print(result)