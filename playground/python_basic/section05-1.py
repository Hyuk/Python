# Section05-1
# 파이썬 흐름제어(제어문)
# 조건문 실습

print(type(True))
print(type(False))

# 예1
if True:
  print("Yes")

if False:
  print("No")
else:
  print("Yes2")

a = 100
b = 60
c = 15

print('and : ', a > b and b > c)
print('or : ', a > b or c > b)