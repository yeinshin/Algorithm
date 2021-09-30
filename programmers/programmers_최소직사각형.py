#https://programmers.co.kr/learn/courses/30/lessons/86491
#프로그래머스-최소직사각형(풀이참고)
def solution(sizes):
    w,h = 0,0
    for a,b in sizes: w,h=max(w,a,b),max(h,min(a,b))
    return w*h