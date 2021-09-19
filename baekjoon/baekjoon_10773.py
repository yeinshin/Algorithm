#https://www.acmicpc.net/problem/10773
#10773번-제로
num = list()
for _ in range(int(input())):
    a = int(input())
    if a!=0: num.append(a)
    else: num.pop()
print(sum(num))