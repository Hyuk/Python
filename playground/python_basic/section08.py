# Section08
# 파이썬 모듈과 패키지

# 패키지 예제
# 상대 경로
# .. : 부모 디렉토리
# .  : 현재 디렉토리

# 사용1(클래스)

from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233

print("ex2 : ", Fibonacci.fib2(400))
# ex2 :  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

# 사용2(클래스) # 권장하지 않음

from pkg.fibonacci import *
Fibonacci.fib(500)

print("ex2 : ", Fibonacci.fib2(600))
# ex2 :  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

print("ex2 : ", Fibonacci().title)
# ex2 :  fibonacci

# 사용3(클래스)
from pkg.fibonacci import Fibonacci as fb

fb.fib(1000)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
print("ex3 : ", fb.fib2(1600))
# ex3 :  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
print("ex3 : ", fb().title)
# ex3 :  fibonacci

# 사용4(함수)
import pkg.calculations as c

print("ex4 : ", c.add(10, 100))
# ex4 :  110
print("ex4 : ", c.mul(10, 100))
# ex4 :  1000

# 사용5(함수)
from pkg.calculations import div as d
print("ex5 : ", int(d(100,10)))
# ex5 :  10

# 사용6
import pkg.prints as p
p.prt1()
# I'm Niceboy!
p.prt2()
# I'm Goodboy!