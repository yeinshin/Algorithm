#https://www.acmicpc.net/problem/14912
#14912번-숫자 빈도구
n,t = map(str,input().split())
result =0 
for i in range(1,int(n)+1):
    i=str(i)
    if t in i:result+=i.count(t)
print(result)