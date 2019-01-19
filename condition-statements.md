# Conditional Statement (if, elif, else)
```python
if 10 > 5:
    print("10이 5보다 크다.")
# 10이 5보다 크다.

my_num = 23
if my_num > 0:
    print(my_num + "은 양수이다.")
elif my_num == 0:
    print(my_num + "은 0이다.")
else:
    print(my_num + "은 음수이다.")

"참이다" if 10 > 5 else "거짓이다"
# '참이다'

"양수이다" if 0 > 0 else ("음수이다" if 0 < 0 else "0이다")
# '0이다'
```