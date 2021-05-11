# list and tuple

### list (순서 O, 중복 O, 수정 O, 삭제 O)

### list Declaration (선언)
```python
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen','Banana','Orange']]
```

### list Indexing (인덱싱)
```python
print(d[3])
# Banana

print(d[-2])
# Banana

print(d[0]+d[1])
# 110

print(e[2][1])
# Banana

print(e[-1][-2])
# Banana
```

### list Slicing (슬라이싱)
```python
print(d[0:3])
# [10, 100, 'Pen']

print(e[2][1:3])
# ['Banana', 'Orange']
```

### list Calculation (연산)
```python
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']

print(c + d)
# [1, 2, 3, 4, 10, 100, 'Pen', 'Banana', 'Orange']

print(c * 3)
# [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

print(str(c[0]) + hi)
# 1hi
```

### list update & delete (수정 & 삭제)
```python
c = [1, 2, 3, 4]

c[0] = 77
print(c)
# [77, 2, 3, 4]

c[1:2] = [100, 1000, 10000]
print(c)
# [77, 100, 1000, 10000, 3, 4]

c[1] = ['a', 'b', 'c']
print(c)
# [77, ['a', 'b', 'c'], 1000, 10000, 3, 4]

del c[1]
print(c)
# [77, 1000, 10000, 3, 4]

del c[-1]
print(c)
# [77, 1000, 10000, 3]
```

### list function (함수)
```python
y = [5, 2, 3, 1, 4]
print(y)
# [5, 2, 3, 1, 4]

y.append(6)
print(y)
# [5, 2, 3, 1, 4, 6]

y.sort()
print(y)
# [1, 2, 3, 4, 5, 6]

y.reverse()
print(y)
# [6, 5, 4, 3, 2, 1]

y.insert(2, 7)
print(y)
# [6, 5, 7, 4, 3, 2, 1]

y.remove(2)
print(y)
# [6, 5, 7, 4, 3, 1]

y.pop()
print(y)
# [6, 5, 7, 4, 3]

ex = [88, 77]
y.extend(ex)
# [6, 5, 7, 4, 3, 88, 77]

y.append(ex)
# [6, 5, 7, 4, 3, 88, 77, [88, 77]]
```