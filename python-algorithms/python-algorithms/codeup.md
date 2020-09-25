# Codeup 

1001. [기초-출력] 출력하기01
Hello
```python
print("Hello")
```

1002. [기초-출력] 출력하기02
Hello World
```python
print("Hello World")
```

1003. [기초-출력] 출력하기03
Hello
World
```python
print("Hello\nWorld")
```

1004. [기초-출력] 출력하기04
'Hello'
```python
print("'Hello'")
```

1005. [기초-출력] 출력하기05
"Hello"
```python
print("\"Hello World\"")
```

1006. [기초-출력] 출력하기06
"!@#$%^&*()"
```python
print("\"!@#$%^&*()\"")
```

1007. [기초-출력] 출력하기07
"C:\Download\hello.cpp"
```python
print("\"C:\Download\hello.cpp\"")
```

1010. [기초-입출력] 정수 1개 입력받아 그대로 출력하기
```python
a=input()
a=int(a)
print(a)
```

1011. [기초-입출력] 문자 1개 입력받아 그대로 출력하기
```python
a=input()
print(a)
```

1012. [기초-입출력] 실수 1개 입력받아 그대로 출력하기
```python
a=input()
a=float(a)
print("%f" % a)
```

1013. [기초-입출력] 정수 2개 입력받아 그대로 출력하기
```python
a,b = input().split()
n=int(a)
m=int(b)
print(a, b)
```

1014. [기초-입출력] 문자 2개 입력받아 순서 바꿔 출력하기
```python
a,b = input().split()
print(b, a)
```

1015. [기초-입출력] 실수 입력받아 둘째 자리까지 출력하기
```python
f=float(input())
print('%.2f' % f)
```

1017. [기초-입출력] 정수 1개 입력받아 3번 출력하기
```python
n=input()
n=int(n)
print(n, n, n,)
```

1018. [기초-입출력] 시간 입력받아 그대로 출력하기
```python
h,m=input().split(':')
print(int(h), int(m), sep=':')
```

1019. [기초-입출력] 연월일 입력받아 그대로 출력하기
```python
a,b,c=input().split('.')

print('%04d' % int(a), end='.')
print('%02d' % int(b), end='.')
print('%02d' % int(c))
```

1020. [기초-입출력] 주민번호 입력받아 형태 바꿔 출력하기
```python
a,b=input().split('-')
print(a+b)
```

1021. [기초-입출력] 단어 1개 입력받아 그대로 출력하기
```python
a=input()
print(a)
```