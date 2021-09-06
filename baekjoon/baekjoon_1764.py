#http://acmicpc.net/problem/1764
#1764번-듣보잡

#듣도 못한 사람의 수:n, 보도 못한 사람의 수:m
n,m = map(int,input().split())
answer = list({input() for _ in range(n)}&{input() for _ in range(m)})
print(len(answer))
print(*sorted(answer),sep='\n') #print('\n'.join(answer))도 가능함

