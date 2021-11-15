#https://www.acmicpc.net/problem/1181
#1181번-단어 정렬
n = int(input())
ans = set()
for _ in range(n):
    w = input()
    ans.add((len(w),w))
ans=sorted(ans)
for i in range(len(ans)):
    print(ans[i][1],end='\n')