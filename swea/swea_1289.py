#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV19AcoKI9sCFAZN
#1289번-원재의 메모리 복구하기

for i in range(1,int(input())+1):
    bit = input()
    tmp = '0'
    cnt = 0
    for b in bit:
        if b!=tmp:
            tmp = b
            cnt+=1
    print('#%d %d'%(i,cnt))