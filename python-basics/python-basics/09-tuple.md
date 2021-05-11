# tuple

### tuple (순서 O, 중복 O, 수정 X, 삭제 X)

```python
a = ()
b = (1, )
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
# 3

print(c[3])
# 4

print(d[2][1])
# b

print(d[2:])
# (('a', 'b', 'c'),)

print(d[2][0:2])
# ('a', 'b')

print(c + d)
# (1, 2, 3, 4, 10, 100, ('a', 'b', 'c'))

print(c * 3)
# (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)
```

### tuple function (함수)
```python
z = (2, 5, 1, 3, 1)

print(z)
# (2, 5, 1, 3, 1)

print(3 in z)
# True

print(z.index(5))
# 1

print(z.count(1))
# 2
```