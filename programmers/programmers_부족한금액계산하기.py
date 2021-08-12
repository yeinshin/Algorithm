#프로그래머스-부족한 금액 계산하기(위클리 챌린지)
def solution(price, money, count):
    cnt = 0
    
    for i in range(1,count+1):
        cnt+= price*i
    
    if cnt < money: return 0
    else: return cnt-money