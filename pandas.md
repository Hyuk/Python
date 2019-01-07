# pandas

```python
import requests
import pandas as pd

response = requests.get("https://api.")
```
```python
df = pdDataFrame([
    item.get("item")
    for item
    in response.json().get("items")
])
```
```python
df.to_csv("zigbang.csv")
df.to_excel("zigbang.xlsx")
```

```python
%matplotlib inline
df.dsposit.hist()
df.rent.hist()
```