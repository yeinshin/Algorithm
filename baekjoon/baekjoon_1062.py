#https://www.acmicpc.net/problem/1062
#1062번-가르침
n,k=map(int,input().split())
s = ['a','n','t','i','c']
words = []
need = set()
ans = 0
for _ in range(n):
    w = set(input()[4:-4])
    a = []
    for i in w: 
        if i not in s: 
            a.append(i)
            need.add(i)
    words.append(a)

if k<5: print(0)
elif 5+len(need)<=k: print(n)
else:
    need = list(need)
    n = len(need)
    k = k-5
    combination = ['']*k

    def combi(now,cnt,k,n):
        global ans
        if cnt==k:
            count = 0
            for i in words:
                check = True
                for j in i:
                    if j not in combination: 
                        check = False
                        break
                if check: count+=1
            ans = max(ans,count)  
            return
        for i in range(now,n):
            combination[cnt] =need[i]
            combi(i+1,cnt+1,k,n)

    combi(0,0,k,n)
    print(ans)