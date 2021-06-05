#https://www.acmicpc.net/problem/1063
#1063번-킹

# R : 한 칸 오른쪽으로
# L : 한 칸 왼쪽으로
# B : 한 칸 아래로
# T : 한 칸 위로
# RT : 오른쪽 위 대각선으로
# LT : 왼쪽 위 대각선으로
# RB : 오른쪽 아래 대각선으로
# LB : 왼쪽 아래 대각선으로

k,d,n = input().split()
moving=list(input() for _ in range(int(n)))

xk,yk,xd,yd = abs(int(k[1])-8), (ord(k[0])-65), abs(int(d[1])-8), (ord(d[0])-65)
dx=[0,0,1,-1,-1,-1,1,1]
dy=[1,-1,0,0,1,-1,1,-1]
direc = ['R','L','B','T','RT','LT','RB','LB']

for m in moving:
    for i in range(8):
        nxk = xk + dx[i]
        nyk = yk + dy[i]

        if m==direc[i] and 0<=nxk<8 and 0<=nyk<8:
            if nxk==xd and nyk==yd: 
                if 0<=xd + dx[i]<8 and 0<=yd + dy[i]<8:
                    xk,yk,xd,yd = nxk,nyk,(xd + dx[i]),(yd + dy[i])
            else:
                xk,yk = nxk,nyk

print(chr(yk+65)+str(abs(xk-8)))
print(chr(yd+65)+str(abs(xd-8)))
