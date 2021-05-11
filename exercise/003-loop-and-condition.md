# loop and condition

* 반복문과 조건문을 이용하여, 다음과 같은 출력이 나오도록 프로그램을 작성하시오.

```
*
**
****
*****
*******
********
```

```python
for num in range(1,9):
  if num %3 != 0:
    print("*"*num)
```

* 반복문과 print() 함수를 이용하여 아래와 같은 출력을 하는 프로그램을 구현하시오.
```
0 1 2 4 8 16 32 64 128 256 256 256
```

```python
array_list = [0]
for num in range(0, 11):
    if num < 9:
        power = 2**num
    else:
        power = 2**8
    array_list.append(power)
    
for elem in array_list:
    print(elem, end=" ")
```