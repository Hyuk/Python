# Inheritance (상속)

* 기본 상속방법

```python
class Animal():

    def eat(self):
        print("먹는다!")

    def attack(self):
        print("공격")

class Dog(Animal):
    def bark(Self):
        print("bowwow")

dog = Dog()

dog.bark()

dog.eat()
```

* Method Overiding - 상속해서 변경하고 싶은 경우
```python
class Animal():

    def eat(self):
        print("먹는다!")

    def attack(self):
        print("공격")

class Dog(Animal):

    def eat(self):
        print("침을 흘리며 먹는다!")
        
    def bark(Self):
        print("bowwow")

dog = Dog()

dog.bark()

dog.eat()
```

# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제1
# 상속 기본

# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능

# 라면 -> 속성(종류, 회사, 맛, 면 종류, 이름) : 부모
```python
class Car:
    """Parent Class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color
        
    def show(self):
        return 'Car Class "Show Mothod!"'
    
class BmwCar(Car):
    """Child Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name
        
    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name
    
class BenzCar(Car):
    """Child Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name
        
    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name
    
    def show(self):
        return 'Car Info %s %s %s' % (self.car_name, self.type, self.color) 
```
# 일반사용
```python
model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color) # Super
# red
print(model1.type) # Super
# sedan
print(model1.car_name) # Sub
# 520d
print(model1.show())
# Car Class "Show Mothod!"
print(model1.show_model())
# Your Car Name : 520d
print(model1.__dict__)
# {'type': 'sedan', 'color': 'red', 'car_name': '520d'}

# Method Overriding(오버라이딩)
model2 = BenzCar("220d",'suv',"black")
print(model2.show())
# Car Info 220d suv black

# Parent Method Call
model3 = BenzCar("350s","sedan","silver")
print(model3.show())
# Car Info 350s sedan silver

# Inheritance Info
print(BmwCar.mro()) # 어떤 클래스를 상속받는지 알려준다.
# [<class '__main__.BmwCar'>, <class '__main__.Car'>, <class 'object'>]
print(BenzCar.mro()) # 상속 정보를 리스트 형태로 반환한다.
# [<class '__main__.BenzCar'>, <class '__main__.Car'>, <class 'object'>]

# 다중 상속
class X():
    pass

class Y():
    pass

class Z():
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z):
    pass

print(M.mro())
# [<class '__main__.M'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class 'object'>]
```