# Functions

### Making a function
```python
def greeting():
    print("Hello World")

greeting()

# Hello World
```

### Passing a single argument
```python
def greeting(name):
    print("Hello, " + name)

greeting("Hyuk")

# Hello, Hyuk
```

### Using a default value
```python
def animal(name, animal='dog'):
    print("I have a " + animal + ".")
    print("Its name is " + name + ".")
animal('willie')

# I have a dog.
# Its name is willie.
```

### Using None to make argument optional
```python
def animal(animal, name=None):
    print("\nI have a "+ animal +".")
    if name:
        print("Its name is "+name+".")
animal('snake')

# I have a snake.
```

### Returning a value
```python
def hello_return(world):
    val = "Hello " + str(world)
    return val

str = hello_return("Python!!!!!")
print(str)
# Hello Python!!!!!
```

### Returning multiple values
```python
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = func_mul(100)
print(val1, val2, val3)
```

### Returning a list
```python
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

lt = func_mul2(100)
print(lt, type(lt))
```

### Returning a tuple
```python
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return (y1, y2, y3)

lt = func_mul2(100)
print(lt, type(lt))
```

### Returning a dictionary
```python
def full_name(first, last):
    person = {'first': first, 'last':last}
    return person

x = full_name('Trilo', 'Chan')
print(x)

# {'first': 'Trilo', 'last': 'Chan'}
```

### Passing a list as an argument
```python
def greet_users(names):
    for name in names:
        msg = "Hello, " + name + "!"
        print(msg)
username = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Hello, hannah!
# Hello, ty!
# Hello, margot!
```

## Basic function with if statement
```python
def check_number(my_number):
    if (my_number > 0):
        print("Number is greater than 0.")
    elif (my_number < 0):
        print("Number is less than 0.")
    else:
        print("Number is equal to 0.")

check_number(0)
# Number is equal to 0.
```
### To store the result of the function
* Use return
```python
def check_number(my_number):
    if (my_number > 0):
        return "Number is greater than 0."
    elif (my_number < 0):
        return "Number is less than 0."
    else:
        return "Number is equal to 0."

result = check_number(0)
result
# 'Number is equal to 0.'
```

### *args, *kwargs
* *args(가변변수) - 변수의 개수가 정해지지 않았을때
```python
def args_func(*args):
    print(args)

args_func('kim')
# ('kim',)
args_func('kim', 'park')
# ('kim', 'park')
args_func('kim','park','lee')
# ('kim', 'park', 'lee')
```

```python
def args_func(*args):
    for t in args:
        print(t)

args_func('kim')
# kim
args_func('kim', 'park')
# kim
# park
args_func('kim','park','lee')
# kim
# park
# lee
```

```python
def args_func(*args):
    for i, v in enumerate(args): # 인덱스를 만들어준다.
        print(i, v)

args_func('kim','park','lee')
# 0 kim
# 1 park
# 2 lee
```

* **kwargs - keyword를 사용, dictionary를 파라미터로 넘길 수 있다.
```python
def kwargs_func(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

kwargs_func(name = 'Kim')
kwargs_func(name1 = 'Kim', name2 = 'Park', name3 = 'Lee')
```

* *args, **kwargs
* *args과 **kwargs는 가변 매개변수로 없어도 그만
```python
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10, 20)
# 10 20 () {}
example_mul(10, 20, 'park', 'kim')
# 10 20 ('park', 'kim') {}
example_mul(10, 20, 'park', 'kim', age1 = 24, age2 = 35)
# 10 20 ('park', 'kim') {'age1': 24, 'age2': 35}
```

### 중첩함수(클로저)
* 함수 안에 함수가 있는 것
```python
def nested_func(num):
    def func_in_func(num):
        print(num)
    print("in func")
    func_in_func(num + 10000)

nested_func(10000)
# in func
# 20000
```

### 매개변수 타입 지정
* 매개변수 타입을 int로 받아서 list 형태로 리턴한다.
```python
def func_mul3(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

print(func_mul3(5))
# [500, 1000, 1500]
```