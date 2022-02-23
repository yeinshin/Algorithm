#https://www.acmicpc.net/problem/6443
#6443번-에너그램 (중복을 없애고 출력을 해야하는 문제 -> 중복을 어떻게하면 바로바로 제거하고 순열을 만들 수 있는지 생각을 하고 문제를 풀자 그렇지 않으면 시간 초과... 그래서 풀이 참고함!)

import sys
input = sys.stdin.readline
def permutations(cnt,n,k):
    global visited
    global s
    global arr
    if cnt==k:
        print("".join(arr))
        return
    for a in visited:
        if visited[a]:
            visited[a] -=1
            arr[cnt] = a
            permutations(cnt+1,n,k)
            visited[a] +=1

m = int(sys.stdin.readline())
for _ in range(m):
    s = sorted(input().rstrip())
    n = len(s)
    visited = {}
    for a in range(n):
        if s[a] in visited: visited[s[a]] += 1
        else: visited[s[a]] = 1
    arr = [0]*n
    permutations(0,n,n)