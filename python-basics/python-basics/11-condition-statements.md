# Conditional Statement (if, elif, else)
```python
if 10 > 5:
    print("10이 5보다 크다.")
# 10이 5보다 크다.

my_num = 23
if my_num > 0:
    print(my_num + "은 양수이다.")
elif my_num == 0:
    print(my_num + "은 0이다.")
else:
    print(my_num + "은 음수이다.")

"참이다" if 10 > 5 else "거짓이다"
# '참이다'

"양수이다" if 0 > 0 else ("음수이다" if 0 < 0 else "0이다")
# '0이다'
```

# 참 거짓 종류(True, False)
# 참: "내용", [내용], (내용), {내용}
# 거짓: "", [], (), {}, 0

```python
city = ""

if city:
    print(">>>True")
else:
    print(">>>False")
# >>>False

cities = "1"

if cities:
    print(">>>>True")
else:
    print(">>>>False")
# >>>>True
```

### 논리 연산자
### and or not
```python
a = 100
b = 60
c = 15

print('and : ', a > b and b > c)
print('or : ', a > b or c > b)
print('not : ', not a > b)
print(not False)
print(not True)
```

### 산술, 관계, 논리 연산자
### 산술 > 관계 > 논리 순서로 적용
```python
print('ex1 : ', 5 + 10 > 0 and not 7 + 3 == 10)
# ex1 : False

score1 = 90
score2 = 'A'

if score1 >= 90 and score2 =='A':
    print("합격하셨습니다.")
else:
    print("죄송합니다. 불합격입니다.")
```

# 다중조건문
```python
num = 90

if num >= 90:
    print("num 등급 A", num)
elif num >= 80:
    print("num 등급 B", num)
elif num >= 70:
    print("num 등급 C", num)
else:
    print("꽝")

```
