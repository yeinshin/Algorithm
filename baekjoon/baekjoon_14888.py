#14888번-연산자 끼워 넣기
#3부<문제>19번-연산자 끼워 넣기
#itertools를 이용한 풀이

from itertools import permutations

n=int(input())
data = list(map(int,input().split()))
add,sub,mul,div = map(int,input().split())

a='+'*add + '-'*sub + '*'*mul + '/'*div
a=list(set(permutations(a,n-1))) 

min_value = 1e9
max_value = -1e9

def calc ():
    global min_value
    global max_value

    for j in range(len(a)):
        result=data[0]
        for i in range(n-1):
            if a[j][i]=='+':
                result+=data[i+1]
            if a[j][i]=='-':
                result-=data[i+1]
            if a[j][i]=='*':
                result*=data[i+1]
            if a[j][i]=='/':
                result=int(result/data[i+1])
        
        min_value=min(min_value,result)
        max_value=max(max_value,result)
    
calc()
print(max_value)
print(min_value)
