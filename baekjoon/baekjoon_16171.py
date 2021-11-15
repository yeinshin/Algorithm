#https://www.acmicpc.net/problem/16171
#16171번-나는 친구가 적다 (Small)

import re
s=input()
print(1 if input() in ''.join(re.findall('[a-zA-Z]+',s)) else 0)