# Inheritance

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