# Leap Year Calculator (윤년계산기)

* 어떤 연도를 N이라고 할 때, N이 윤년인지 아닌지 알아보는 방법은 무엇일까?
* 윤년 규칙. N이 4의 배수이면서, 100의 배수가 아니거나 400의 배수면 윤년이다.

```python
year = 2021

((year % 4 == 0) and (year % 100 != 0 )) or (year % 400 == 0)

# True
```