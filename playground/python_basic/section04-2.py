# Section04-2
# 문자열, 문자열연산, 슬라이싱

str1 = "I am Boy."
str2 = 'NiceMan'
str3 = ''
str4 = str('')

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


b = (1, )
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))


print(c[2])
print(c[3])
print(d[2][1])

print(d[2:])
print(d[2][0:2])

z = (2, 5, 1, 3, 1)

print(z)
# (2, 5, 1, 3, 1)

print(3 in z)
# True

print(z.index(5))
# 1

print(z.count(1))
# 2

a = {'name': 'Kim', 'Phone': '010-7777-7777', 'birth': '870214'}
a['address'] = 'Seoul'
print(a)
# {'name': 'Kim', 'Phone': '010-7777-7777', 'birth': '870214', 'address':'Seoul'}

a['rank'] = [1, 3, 4]
a['rank2'] = (1, 2, 3,)
print(a)

print(a.keys())