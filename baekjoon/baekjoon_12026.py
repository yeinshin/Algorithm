#https://www.acmicpc.net/problem/12026
#12026번-BOJ 거리

n= int(input())
block = list(input())
B,O,J = [],[],[]
dp = [1000001]*n
dp[0]=0

for i,v in enumerate(block):
    if v =='B':
        B.append(i)
    if v =='O':
        O.append(i)
    if v =='J':
        J.append(i)
def check (array1,array2,i):
    for a in array1:
        if a>=i:
            for b in array2:
                if a>b:
                    dp[a]=min((a-b)**2+dp[b],dp[a])

before = 'B'
for i in range(1,n):
    if before == 'B' and block[i]=='O':
        check(O,B,i)
        before = block[i] 
    elif before == 'O' and block[i]=='J':
        check(J,O,i)
        before = block[i] 
    elif before == 'J' and block[i]=='B':
        check(B,J,i)
        before = block[i] 
        
if dp[n-1]==1000001: print(-1)
else: print(dp[n-1])

      
