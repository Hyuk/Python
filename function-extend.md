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
def get_sum(*args):
    result = 0
    for arg in args:
        result += arg
    return result

get_sum(1,2,3,4,5)

# 15
```