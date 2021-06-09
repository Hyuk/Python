# Class 클래스
* 파이썬 클래스 상세 이해
* Self, 클래스, 인스턴스 변수
* 클래스, 인스턴스 차이 중요
* 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
* 클래스 변수 : 직접 사용 가능, 객체 보다 먼저 생성
* 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

### 선언
```python
class UserInfo:
    # 속성, 메소드
    def __init__(self, name):
        self.name = name
    def user_info_p(self):
        print("Name : ", self.name)

# 네임스페이스 (user1, user2) (user1 != user2)
user1 = UserInfo("Kim")
user1.user_info_p()
# Name :  Kim
user2 = UserInfo("Park")
user2.user_info_p()
# Name :  Park

print(id(user1))
# 1950222607920
print(id(user2))
# 1950222608088
print(user1.__dict__)
# {'name': 'Kim'}
print(user2.__dict__)
# {'name': 'Park'}
```

### self의 이해
```python
class SelfTest:
    def function1():
        print('function1 called!')
    def function2(self):
        print('function2 called!')

self_test = SelfTest()
# self_test.function1() # self 매개변수가 없어서 에러가 난다.
SelfTest.function1() # function1 called!
self_test.function2() # function2 called!

print(id(self_test))
SelfTest.function2(self_test) # function2 called!
```

### 클래스 변수, 인스턴스 변수
* 클래스 변수는 self가 없고, 인스턴스 변수는 self가 있다.

```python
class WareHouse:
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(user1.__dict__)
# {'name': 'Kim'}
print(user2.__dict__)
# {'name': 'Park'}
print(user3.__dict__)
# {'name': 'Lee'}
print(WareHouse.__dict__) # 클래스 네임스페이스, 클래스 변수(공유)
# {'__module__': '__main__', 'stock_num': 3, '__init__': <function WareHouse.__init__ at 0x000002BAE830EF70>, '__del__': <function WareHouse.__del__ at 0x000002BAE830E940>, '__dict__': <attribute '__dict__' of 'WareHouse' objects>, '__weakref__': <attribute '__weakref__' of 'WareHouse' objects>, '__doc__': None}
print(user1.name)
# Kim
print(user2.name)
# Park
print(user3.name)
# Lee
print(user1.stock_num)
# 3
del user1
print(user2.stock_num)
# 2
print(user3.stock_num)
# 2
```


```python
class Person():
    
    def __init__(self, name, age, *args, **kwargs):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hi, I am {age} years old and my name is {name}.".format(age=self.age, name=self.name))

data = [
    {"name": "사람1", "age": 30},
    {"name": "사람2", "age": 30},
    {"name": "사람3", "age": 30}
]

people = [
    Person(person["name"],person["age"])
    for person
    in data
]

people[1].introduce()

# Hi, I am 30 old and my name is 사람2.
```

```python
class Person():
    
    def __init__(self, name, age, *args, **kwargs):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hi, I am {age} years old and my name is {name}.".format(age=self.age, name=self.name))

    def meet(self, another):
        print("{myname}이 {partner_name}을 만났습니다!".format(
            myname = self.name,
            partner_name = another.name
        ))

hyuk = Person("hyuk", 34)
kuyh = Person("kuyh", 28)
hyuk.meet(kuyh)

# hyuk이 kuyh을 만났습니다!
```

```python
class Person():
    
    def __init__(self, name, age, money, *args, **kwargs):
        self.name = name
        self.age = age
        self.money = money

    def introduce(self):
        print("Hi, I am {age} years old and my name is {name}.".format(age=self.age, name=self.name))

    def give(self, partner, amount):
        self.money -= amount
        partner.money += amount

hyuk = Person("hyuk", 34, 1000)
kuyh = Person("kuyh", 28, 5000)

# kuyh => hyuk (2000)

kuyh.give(hyuk,2000)

hyuk.money # 3000
kuyh.money # 3000
```

```python
class Person():
    
    def __init__(self, name, age, money, *args, **kwargs):
        self.name = name
        self.age = age
        self.money = money

    def __str__(self): # class의 기본 정보 확인
        return self.name

    def introduce(self):
        print("Hi, I am {age} years old and my name is {name}.".format(age=self.age, name=self.name))

    def give(self, partner, amount):
        self.money -= amount
        partner.money += amount

hyuk = Person("hyukho", 34, 1000)

print(hyuk)
```

## 클래스의 덧샘기능 추가
```python
class Person():
    
    def __init__(self, name, age, money, *args, **kwargs):
        self.name = name
        self.age = age
        self.money = money

    def __str__(self):
        return self.name

    def __add__(self, partner):
        print("{name} & {partner_name} | 결혼을 축하합니다.".format(
            name = self.name,
            partner_name = partner.name
        ))

    def introduce(self):
        print("Hi, I am {age} years old and my name is {name}.".format(age=self.age, name=self.name))

    def give(self, partner, amount):
        self.money -= amount
        partner.money += amount

hyuk = Person("hyuk", 34, 1000)
kuyh = Person("kuyh", 28, 5000)

hyuk + kuyh

```


## Triangle Class

```python
class Triangle():
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "{width}, {height} Triangle".format(
            width=self.width, height=self.height
        )

t1 = Triangle(10,20)
print(t1)

# 10, 20 Triangle
```

```python
class Triangle():
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "{width}, {height} Triangle".format(
            width=self.width, height=self.height
        )

    def area(self):
        return self.width*self.height*0.5

    def is_bigger_than(self, another):
        return self.area() > another.area()
t1 = Triangle(10,20)
t2 = Triangle(20,40)

t1.is_bigger_than(t2)
# False
```