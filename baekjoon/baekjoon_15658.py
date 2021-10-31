#https://www.acmicpc.net/problem/15658
#15658번-연산자 끼워넣기(2)

n = int(input())
nums = list(map(int,input().split()))
#+, -, *, // (나눗셈은 정수 나눗셈으로 몫만 취한다)
#음수를 양수로 나눌 때는 양수로 바꾼 뒤 몫을 구하고 그 몫을 음수로 바꾼 것과 같다
calc = list(map(int,input().split()))
dic = {'+':0,'-':1,'*':2,'/':3}

INF = int(1e9)
max_value = -INF
min_value = INF

# 값 계산해주는 함수
def calculation(s):
    cnt = nums[0]
    for i in range(n-1):
        if s[i]=='+': cnt+=nums[i+1]
        elif s[i]=='-':cnt-=nums[i+1]
        elif s[i]=='*':cnt*=nums[i+1]
        else: 
            if cnt<0: cnt = -((-cnt)//nums[i+1])
            elif nums[i+1]<0: cnt = -(cnt//(-nums[i+1]))
            else: cnt//=nums[i+1]
    return cnt

#백트래킹
def dfs(cnt,s):
    global max_value
    global min_value
    if cnt==n-1:
        value = calculation(s)
        max_value = max(max_value,value)
        min_value = min(min_value,value)
        return
    for i in ('+','-','*','/'):
        if calc[dic[i]]-1>-1:
            calc[dic[i]]-=1
            dfs(cnt+1,s+i)
            calc[dic[i]]+=1
dfs(0,'')
print(max_value,min_value,sep='\n')
