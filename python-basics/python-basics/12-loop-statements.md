# Loops Statement (for loop, do while loop)

### while loop
```python
v1 = 1
while v1 < 11:
    print("v1 is :", v1)
    v1 += 1

# v1 is : 1
# v1 is : 2 
# v1 is : 3 
# v1 is : 4 
# v1 is : 5 
# v1 is : 6 
# v1 is : 7 
# v1 is : 8 
# v1 is : 9 
# v1 is : 10
```

### while loop - 1 ~ 100 합
```python
sum1 = 0
cnt1 = 1
while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print('1 ~ 100 : ', sum1)
# 1 ~ 100 : 5050
```

### 1 ~ 100 합
```python
print('1 ~ 100 : ', sum(range(1, 101)))
# 1 ~ 100 : 5050
```

### 1 ~ 100 (1, 3, 5, ... 99) 합
```python
print('1 ~ 100 : ', sum(range(1, 101, 2)))
# 1 ~ 100 :  2500
```

### for loop
```python
for i in range(10): # 0부터 (n-1) -> 0,1,2,3,4,5,6,7,8,9
    print(i)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

for i in range(1, 11): # 시작: 1, 마지막 (11-1)
    print(i)
# 1
# 2 
# 3 
# 4 
# 5 
# 6 
# 7 
# 8 
# 9 
# 10
```

### For Loop 을 사용해서 구구단을 표시하는 방법
```python
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = ' % (i,j), i*j)
```

### 시퀀스(순서가 있는) 자료형 반복
### 문자열, 리스트, 튜플, 집합, 사전
### iterable 리턴 함수: range, reversed, enumerate, filter, map, zip

```python
names = ["Kim", "Park", "Cho", "Choi", "Yoo"]

for v in names:
    print("You are : ", v)

# You are :  Kim
# You are :  Park
# You are :  Cho 
# You are :  Choi
# You are :  Yoo 

word = "dreams"

for s in word:
    print("Word : ", s)

# Word :  d      
# Word :  r      
# Word :  e      
# Word :  a      
# Word :  m      
# Word :  s

my_info =  {
    "name": "Kim",
    "age" : 33, 
    "city": "Seoul"
}

for key in my_info:
    print("my_info", key)

# my_info name
# my_info age
# my_info city

for key in my_info.values():
    print("my_info", key)

# my_info Kim
# my_info 33
# my_info Seoul

for key in my_info.keys():
    print("my_info", key)

# my_info name
# my_info age
# my_info city
```

```python
# For loop을 사용해서 List 데이터 표시하기
animals = ["강아지", "고양이", "물고기"]
for animal in animals:
    print(animal + "을/를 키우고 있습니다.")

# 강아지을/를 키우고 있습니다.
# 고양이을/를 키우고 있습니다.
# 물고기을/를 키우고 있습니다.

# For loop을 사용해서 Dist 데이터 표시하기
student = student = {"name": "Hyuk", "age": "20", "email": "hyukho83@gmail.com"}
for key in student:
    value = student[key]
    # print(value)
    print(key + " => " + str(student[key]))

for key, value in student.items():
    print(key + " => " + str(value))


```

