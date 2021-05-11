# dictionary

### dictionary (순서 X, 중복 X, 수정 O, 삭제 O)


### Key, Value (JSON) -> MongoDB


### dictionary declairation
```python
a = {'name': 'Kim', 'Phone': '010-7777-7777', 'birth': '870214'}
b = {0: 'Hello Python', 1: 'Hello Coding'}
c = {'arr': [1, 2, 3, 4, 5}

# print(type(a))
```

### print
```python
print(a['name'])
# Kim

print(a.get('name'))
# Kim

print(a.get('address'))
# None

print(c['arr'][1:3])
# [2, 3]
```

### Insert
```python
a['address'] = 'Seoul'
print(a)
# {'name': 'Kim', 'Phone': '010-7777-7777', 'birth': '870214', 'address':'Seoul'}

a['rank'] = [1, 3, 4]
a['rank2'] = (1, 2, 3,)
print(a)
# {'name': 'Kim', 'Phone': '010-7777-7777', 'birth': '870214', 'address': 'Seoul', 'rank': [1, 3, 4], 'rank2': (1, 2, 3)}

print(a.keys())
# dict_keys(['name', 'Phone', 'birth', 'address', 'rank', 'rank2'])
```