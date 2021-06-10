# Module and Package

* pkg 폴더 하위에 __init__.py를 생성
  * 용도 : 해당 디렉토리가 패키지임을 선언한다.
  * Python 3.x : 파일이 없어도 패키지 인식함 -> 하위호환 위해서 생성해놓은 것을 추천함.

# pkg 폴더 하위에 fibonacci.py를 생성하여 다음과 같이 작성
```python
class Fibonacci:
    def __init__(self, title="fibonacci"):
        self.title = title
        
    def fib(n):
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a + b
        print()
        
    def fib2(n):
        result = []
        a, b = 0, 1
        while a < n:
            result.append(a)
            a, b = b, a + b
        return result
```

# pkg 폴더 하위에 prints.py를 생성하여 다음과 같이 작성
```python
def prt1():
  print("I'm Niceboy!")

def prt2():
  print("I'm Goodboy!")

# 단위 실행(독립적으로 파일 실행)
if __name__ == "__main__":
  prt1()
  prt2()

```

# pkg 폴더 하위에 calculations.py를 생성하여 다음과 같이 작성
```python
def add(l, r):
  return l+r

def mul(l, r):
  return l*r

def div(l, r):
  return l/r
```
```python
# 사용1(클래스)

from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233

print("ex2 : ", Fibonacci.fib2(400))
# ex2 :  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

# 사용2(클래스) # 권장하지 않음

from pkg.fibonacci import *
Fibonacci.fib(500)

print("ex2 : ", Fibonacci.fib2(600))
# ex2 :  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

print("ex2 : ", Fibonacci().title)
# ex2 :  fibonacci

# 사용3(클래스)
from pkg.fibonacci import Fibonacci as fb

fb.fib(1000)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
print("ex3 : ", fb.fib2(1600))
# ex3 :  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
print("ex3 : ", fb().title)
# ex3 :  fibonacci

# 사용4(함수)
import pkg.calculations as c

print("ex4 : ", c.add(10, 100))
# ex4 :  110
print("ex4 : ", c.mul(10, 100))
# ex4 :  1000

# 사용5(함수)
from pkg.calculations import div as d
print("ex5 : ", int(d(100,10)))
# ex5 :  10

# 사용6
import pkg.prints as p
p.prt1()
# I'm Niceboy!
p.prt2()
# I'm Goodboy!

# 사용7(내장함수)
import builtins
print(dir(builtins))
# ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
```