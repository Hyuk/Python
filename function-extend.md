# Function Extend
* 보통의 함수들은 인자 값을 받는 변수가 정해서 받기 때문에 확장성이 없다.
* 인자 값 확장 가능한 함수를 만들어 보고자 한다

## *arg **kwarg

```python
def get_sum(*args): # 인자값의 수에 구애받지 않고 확장이 가능한 함수를 구현한다
    print(args)

get_sum(1,2,3)

# (1,2,3)
```

```python
def get_sum(*args):  # 함수를 정의할 때 "*" => 인자값을 하나로 묶어주는 기능 "Pack"이라 부른다. 이름보다 "*" 표시가 중요하다
    result = 0
    for arg in args:
        result += arg
    return result

get_sum(1,2,3,4,5)

# 15
```

* 만약 리스트를 함수 인자값으로 받는 다면 오류가 나게 되는데 
* 리스트를 호출할 떄는 인자변수 앞에 "*"을 붙여서 호출한다.
* "*" => pack && unpack

```python
def get_sum(*args):
    result = 0
    for arg in args:
        result += arg
    return result

numbers = [1,2,3,4,5]
get_sum(*numbers)

# 15
```

## *args and **kwargs
* *args (여러개의 인자 ... => tuple)
* **kwargs (여러개의 인자 그런데 이름이 있다! (Keyword Argument) => dict)

```python
def hello(**kwargs):
    print(kwargs)

hello(name="Hyuk", email="hyukho83@gmail.com")
```


* **kwargs는 보통 list of dictionary를 인자값으로 돌릴때 사용한다.
```python
def hello(**kwargs):
    print(kwargs)
student = {
    "name": "Hyuk",
    "email": "hyukho83@gmail.com"
}
hello(student) # 오류 발생
hello(*student) # 오류 발생
hello(**student) # list of dictionary를 인자값으로 사용할 때 **을 붙인다.
```

* *arg와 **kwargs를 같이 사용해보자
```python
def hello(*args,**kwargs):
    print(args)
    print(kwargs)

hello(1,2,3,name="hyuk")
# (1, 2, 3)
# {'name': 'hyuk'}

```

* 필수정보 포함해서 *arg와 **kwargs를 같이 사용해보자
```python
def hello(name, email, *args, **kwargs):
    print("안녕하세요. " + name + "입니다.")
    print("이메일은 " + email + "입니다.")
    print("--------------------------------")
    print(kwargs)
    print("--------------------------------")

hello("Hyuk", "hyukho83@gmail.com")

# 안녕하세요. Hyuk입니다.
# 이메일은 hyukho83@gmail.com입니다.
# --------------------------------
# {}
# --------------------------------
```

```python
def hello(name, email, *args, **kwargs):
    print("안녕하세요. " + name + "입니다.")
    print("이메일은 " + email + "입니다.")
    print("--------------------------------")
    print(kwargs)
    print("--------------------------------")

hello("Hyuk", "hyukho83@gmail.com", phonenumber="123456789")

# 안녕하세요. Hyuk입니다.
# 이메일은 hyukho83@gmail.com입니다.
# --------------------------------
# {'phonenumber': '123456789'}
# --------------------------------

```
