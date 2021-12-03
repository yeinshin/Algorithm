#https://www.acmicpc.net/problem/9372
#9327번-상근이의 여행(풀이참고)-> 모든 노드가 항상 연결 -> 노드수 -1이 항상 답이다

for _ in range(int(input())):
    n,m = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(m)]
    print(n-1)