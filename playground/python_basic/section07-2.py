# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제1
# 상속 기본

# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속서, 메소드 사용 가능

# 라면 -> 속서(종류, 회사, 맛, 면 종류, 이름) : 부모

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
    
# 일반사용
model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color) # Super
print(model1.type) # Super
print(model1.car_name) # Sub
print(model1.show())
print(model1.show_model())
print(model1.__dict__)

# Method Overriding(오버라이딩)
model2 = BenzCar("220d",'suv',"black")
print(model2.show())

# Parent Method Call
model3 = BenzCar("350s","sedan","silver")
print(model3.show())

# Inheritance Info
print(BmwCar.mro()) # 어떤 클래스를 상속받는지 알려준다.
print(BenzCar.mro()) # 상속 정보를 리스트 형태로 반환한다.

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



