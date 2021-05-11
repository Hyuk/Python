# 

* 다음 동작 수행하는 프로그램을 작성하시오. (단, 입력 a의 내용이 아래 예시 입력과 달라져도 프로그램이 동작해야 한다.)
  * 최대 인원 수가 정해진 방과후 수업에 학생들을 배정하려고 한다.
  * 학생들은 각자 원하는 스포츠 종목을 적어냈고, 해당 종목들은 리스트 a에 저장되어 있다.
  * 방과후 수업에는 최대 정원이 있어, 파이썬 프로그램을 이용해 자료를 처리하고자 한다. 각 스포츠 종목별로 지원자의 수를 출력하는 프로그램을 작성하시오.

* result
```python
a = ['base ball', 'basket ball', 'soccer', 'base ball', 'soccer', 'soccer', 'basket ball', 'base ball', 'basket ball', 'soccer', 'basket ball', 'basket ball', 'base ball', 'soccer', 'soccer', 'basket ball', 'basket ball', 'base ball', 'base ball']
```

```python
def lenthSort(a):
    return len(a)

a = ['base ball', 'basket ball', 'soccer', 'base ball', 'soccer', 'soccer', 'basket ball', 'base ball', 'basket ball', 'soccer', 'basket ball', 'basket ball', 'base ball', 'soccer', 'soccer', 'basket ball', 'basket ball', 'base ball', 'base ball']
b = list(set(a))
print(b)
b.sort(reverse=True, key=lenthSort)
for sport in b:
    print(sport, a.count(sport))
```