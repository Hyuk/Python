# String function

### 문자열 함수
* [https://www.w3schools.com/python/python_ref_string.asp](https://www.w3schools.com/python/python_ref_string.asp)

```python
str1 = "I am Boy."
str2 = 'NiceMan'
str3 = ''
str4 = str('')

# 문자열 길이
print(len(str1), len(str2), len(str3), len(str4))
# 9 7 0 0

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
# Do you have a "big collection"

escape_str2 = "Tab\tTab\tTab"
print(escape_str2)
# Tab     Tab     Tab

# Raw String
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)
# C:\Programs\Test\Bin

raw_s2 = r"\\a\\a"
print(raw_s2)
# \\a\\a

# Multi Line
multi = \
"""
문자열
멀티라인
테스트
"""
print(multi)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = 'def'
str_o4 = "Niceman"

print(str_o1 * 100)
print(str_o2 + str_o3)
print(str_o1 * 3)

print('a' in str_o4)
# True

print('f' in str_o4)
# False

print('z' not in str_o4)
# True
```


```python
a = 'niceman'
b = 'orange'
c = 'Niceman'

# 모두 소문자 인지 확인
print(a.islower())
# True

print(c.islower())
# False

# 마지막 글자가 특정 문자로 끝나는지 확인
print(a.endswith('s'))
# False

print(b.endswith('e'))
# True

# 단어의 첫글자를 대문자로 변경
print(a.capitalize())
# Niceman

# 단어 변경
print(a.replace('nice','good'))
# goodman

# 단어를 역순으로해서 리스트로 반환
print(list(reversed(b)))
# ['e','g','n','a','r','o']
```

### 문자열 슬라이싱
```python
a = 'niceman'
b = 'orange'

print(a[0:3])
# nic

print(a[0:4])
# nice

print(a[0:len(a)])
# niceman

print(a[:4])
# nice

print(a[:])
# niceman

print(b[0:4:2])
# oa

print(b[1:-2])
# ran

print(b[::-1])
# egnaro
```