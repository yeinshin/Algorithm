#https://www.acmicpc.net/problem/5597
#5597번-과제 안 내신 분..?
print(*sorted(set(range(1,31))-set(int(input()) for m in range(28))),sep='\n')