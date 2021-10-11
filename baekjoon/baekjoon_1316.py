#https://www.acmicpc.net/problem/1316
#1316번-그룹 단어 체커
n = int(input())
words = [input() for _ in range(n)]
answer = 0
for word in words:
    check = []
    result = False
    for a,b in enumerate(word):
        check.append((b,a))
    check.sort()
    for i in range(len(check)-1):
        if check[i][0]==check[i+1][0] and check[i+1][1]-check[i][1]!=1:
            result = True
            break
    if not result : answer+=1
print(answer)
            