# 1978 수학은 비대면 강의입니다

import sys 

input = sys.stdin.readline
a, b, c, d, e, f = map(int, input().split())

den = a*e - b*d
x = (c*e - b*f) // den
y = (a*f - c*d) // den

print(x, y)