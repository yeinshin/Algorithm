#1057번-토너먼트/해설 참고함

#참가자의 수 N과 1 라운드에서 김지민의 번호와 임한수의 번호가 순서대로 주어진다.
n,kim,im = map(int,input().split())
cnt = 0

while kim!=im:
    kim-= kim//2
    im-= im//2

    cnt+=1

print(cnt)