# Class 클래스

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