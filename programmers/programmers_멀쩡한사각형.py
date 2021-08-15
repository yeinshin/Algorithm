#프로그래머스-멀쩡한 사각형(풀이 참고)

import math
def solution (w,h):
    return w*h-(w+h-math.gcd(w,h))