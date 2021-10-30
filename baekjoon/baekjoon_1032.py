#https://www.acmicpc.net/problem/1032
#1032번-명령 프롬프트
n = int(input())
s = [input() for _ in range(n)]
result=''
for j in range(len(s[0])):
    check = False
    for i in range(n-1):
        if s[i][j]!=s[i+1][j]: 
            check = True
            break
    result+='?' if check else s[i] 
print(result)
    