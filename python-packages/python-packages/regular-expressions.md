# Regular Expressions
* [Python official doc](https://docs.python.org/3/library/re.html)
* [w3schools Python RegEx](https://www.w3schools.com/python/python_regex.asp)


### import regular expressions library
```python
import re
```

### compile
* String Pattern

```python
# . (ca.e) : One Character : care, cafe, case (O) | caffe (X)
# ^ (^de)  : Start letter : desk, destination (O) | fade (X)
# $ (se$)  : End letter : case, base (O) | fases (X)
```

### match
* compare the string with string pattern from the beggining of the string.

```python
p = re.compile("ca.e")
m = p.match("case")
print(m.group()) # if it doesn't match, display error otherwise print the match string.
```

### group
* the part of the string match with the pattern

```python
def print_match(m):
  if m:
    print(m.group())
  else:
    print("it doesn't match")

p = re.compile("ca.e")
m = p.match("careless")
print_match(m)

# care
```

```python
def print_match(m):
  if m:
    print(m.group())
  else:
    print("it doesn't match")

p = re.compile("ca.e")
m = p.match("life care")
print_match(m)

# it doesn't match
```

### search
* compare the string with the string pattern and if it has the 

```python
def print_search(m):
  if m:
    print(m.group())
  else:
    print("it doesn't match")

p = re.compile("ca.e")
m = p.search("life care")
print_search(m)

# care
```

### group
* return the part of the string match with the pattern
### string
* return the all string if the string match with the pattern
### start
* return the first index of the part of the string match with the pattern 
### end
* return the last index of the part of the string match with the pattern
### span
* return the tuple of first index and the last index of the part of the string match with the pattern

```python
def print_search(m):
  if m:
    print("m.group()", m.group())
    print("m.string", m.string)
    print("m.start()", m.start())
    print("m.end()", m.end())
    print("m.span()", m.span())
  else:
    print("it doesn't match")

p = re.compile("ca.e")
m = p.search("life care")
print_search(m)

# m.group() care
# m.string life care
# m.start() 5
# m.end() 9
# m.span() (5, 9)
```

### findall
* return the list of the match part of the string.

```python
p = re.compile("ca.e")
lst = p.findall("good care cafe") # findall
print(lst)

# ['care', 'cafe']
```