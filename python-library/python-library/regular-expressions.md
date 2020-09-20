# Regular Expressions

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
