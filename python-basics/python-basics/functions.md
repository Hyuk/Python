# Functions

### Making a function
```python
def greeting():
    print("Hello World")

greeting()

# Hello World
```

### Passing a single argument
```python
def greeting(name):
    print("Hello, " + name)

greeting("Hyuk")

# Hello, Hyuk
```

### Using a default value
```python
def animal(name, animal='dog'):
    print("I have a " + animal + ".")
    print("Its name is " + name + ".")
animal('willie')

# I have a dog.
# Its name is willie.
```

### Using None to make argument optional
```python
def animal(animal, name=None):
    print("\nI have a "+ animal +".")
    if name:
        print("Its name is "+name+".")
animal('snake')

# I have a snake.
```

### Returning a dictionary
```python
def full_name(first, last):
    person = {'first': first, 'last':last}
    return person

x = full_name('Trilo', 'Chan')
print(x)

# {'first': 'Trilo', 'last': 'Chan'}
```

### Passing a list as an argument
```python
def greet_users(names):
    for name in names:
        msg = "Hello, " + name + "!"
        print(msg)
username = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Hello, hannah!
# Hello, ty!
# Hello, margot!
```

## Basic function with if statement
```python
def check_number(my_number):
    if (my_number > 0):
        print("Number is greater than 0.")
    elif (my_number < 0):
        print("Number is less than 0.")
    else:
        print("Number is equal to 0.")

check_number(0)
# Number is equal to 0.
```
### To store the result of the function
* Use return
```python
def check_number(my_number):
    if (my_number > 0):
        return "Number is greater than 0."
    elif (my_number < 0):
        return "Number is less than 0."
    else:
        return "Number is equal to 0."

result = check_number(0)
result
# 'Number is equal to 0.'
```

## Functions related with String
* split
* join
* replace
* startswith
* endswith

### split
String을 Seperator를 기준으로 나누고 List 형태로 반환한다.
```python
data = "123,hello,world,78,pass"
data.split(",")
# ['123', 'hello', 'world', '78', 'pass']
```

### join
```python
data2 = ['123', 'hello', 'world']
"-".join(data2)
# '123-hello-world'
```

### split <=> join

### replace
```python
data = "123,hello,world,78,pass"
data.replace(",","|")
# '123|hello|world|78|pass'
```

### in
check the string has the letters inside
```python
data = "123,hello,world,78,pass"
"ello" in data
# True
```

### startswith
```python
data = "123,hello,world,78,pass"
data.startswith("12")
# True
```

### endswith
```python
data = "123,hello,world,78,pass"
data.endswith("ass")
# True
```

## List 관련 함수들
* append()
* extend()
* += operator
* sort()
* reverse()
* sorted()
* sum()

### append()
* List에 새로운 데이터 한개를 추가할 때
```python
animals = []
animals.append("dog")
animals
# ['dog']
animals.append("cat")
animals
# ['dog', 'cat']
```

### extend()
* List에 새로운 여러개의 데이터를 추가할 떄
* 서로 다른 리스트를 합칠 때 사용한다.
```python
myList = [1,2,3]
myCollection = [4,5,6]
myList.extend(myCollection)
myList
# [1,2,3,4,5,6]
```
* append() 함수를 사용하면 Sub List형태로 들어간다.
```python
myList = [1,2,3]
myCollection = [4,5,6]
myList.append(myCollection)
myList
# [1,2,3,[4,5,6]]
```

### += operator
* 
```python
myList = [1,2,3]
myValue = 2
myList += [myValue]
myList
# [1, 2, 3, 2]
myList = [1,2,3]
myCollection = [4,5]
myList += myCollection
myList
# [1, 2, 3, 4, 5]
```

### sort()
* List 오름차순 정령
```python
myList = [4,6,9,0,3,7,4,2,1]
myList.sort()
myList
# [0, 1, 2, 3, 4, 4, 6, 7, 9]
```

### reverse()
* List 역순 정렬
```python
myList = [4,6,9,0,3,7,4,2,1]
myList.reverse()
myList
# [1, 2, 4, 7, 3, 0, 9, 6, 4]
```

### sorted()
```python
myList = []
toSortList = [4,8,4,2,1,0,5]
myList = sorted(toSortList)
myList
# [0, 1, 2, 4, 4, 5, 8]
```

### sum()
```python
toSortList = [4,8,4,2,1,0,5]
sum(toSortList)
# 24
```

## Dict 관련 함수들
* get

### get
* 학생 1000명을 for 문 돌다가, address 가 있으면 address를 출력하고, 없으면 "주소 없음" 이라고 출력하자.
```python
student = {"name": "Hyuk", "email": "email@email.com"}
student["name"]
# Hyuk
student.get("address","주소 없음")
# 주소 없음
```