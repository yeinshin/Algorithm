#https://www.acmicpc.net/problem/1010
#1010번-다리 놓기

import math
T=int(input())
for _ in range(T):
    #mCn
    n,m = map(int,input().split())   

    #mCn=m!/(n!*(m-n)!)
    answer=math.factorial(m)//(math.factorial(n)*math.factorial(m-n))
    
    print(answer)