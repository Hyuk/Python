# Class

```python
class Person():
    
    def __init__(self, name, age, *args, **kwargs):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hi, I am {age} years old and my name is {name}.".format(age=self.age, name=self.name))

data = [
    {"name": "사람1", "age": 30},
    {"name": "사람2", "age": 30},
    {"name": "사람3", "age": 30}
]

people = [
    Person(person["name"],person["age"])
    for person
    in data
]

people[1].introduce()

# Hi, I am 30 old and my name is 사람2.
```