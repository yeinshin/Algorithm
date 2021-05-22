#https://www.acmicpc.net/problem/1120
#1120번-문자열/해설 참고한 문제

#A와 B의 길이가 같으면서, A와 B의 차이를 최소가 되도록 했을 때, 그 차이를 출력하시오.
#len(A) <= len(B)

a,b = input().split()

min_result = 50
while len(a)<=len(b):
    cnt=0
    for i in range(len(a)):
        if a[i]!=b[i]:
            cnt+=1
        
    min_result =  min(min_result,cnt)

    del b[0]

print(min_result)
        
    

