s# Loops Statement (for loop, do while loop)
```python
for i in range(10): # 0부터 (n-1) -> 0,1,2,3,4,5,6,7,8,9
    print(i)
#
0
1
2
3
4
5
6
7
8
9

# For loop을 사용해서 List 데이터 표시하기
animals = ["강아지", "고양이", "물고기"]
for animal in animals:
    print(animal + "을/를 키우고 있습니다.")

# 강아지을/를 키우고 있습니다.
# 고양이을/를 키우고 있습니다.
# 물고기을/를 키우고 있습니다.

# For loop을 사용해서 Dist 데이터 표시하기
student = student = {"name": "Hyuk", "age": "20", "email": "hyukho83@gmail.com"}
for key in student:
    value = student[key]
    # print(value)
    print(key + " => " + str(student[key]))

for key, value in student.items():
    print(key + " => " + str(value))


```