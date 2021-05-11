# Pandas

* The Pandas library is built on NumPy and provides easy-to-use data structures and data analysis tools for the Python programming language.

* Use the following import convention:
```python
import pandas as pd
```

### Pandas Data Structures
* Series: A one-dimensionallabeled array capable of holding any data type
```python
s = pd.Series([3, -5, 7, 4], index=['a','b','c','d'])
```

* DataFrame: A two-dimensional labeled data structure with columns of potentially different types
```python
data = {
  'Country': ['Belgium','India','Brazil'],
  'Capital': ['Brussels', 'New delhi', 'Brasília'],
  'Population: [[11190846, 1303171035, 207847528]
}

df = pd.DataFrame(data, columns=['Country', 'Capital', 'Population'])
```

### I/O Input and Output
* Read and Write to CSV
```python
pd.read_csv('file.csv', header=None, nrows=5)
df.to_csv('nyDataFrame.csv')
```

* Read and Write to Excel
```python
pd.read_excel('file.xlsx')
df.to_excel('dir/myDataFrame.xlsx', sheet_name='Sheet1')
```

* Read multiple sheets from the same file
```python
xlsx = pd.ExcelFile('file.xls')
df = pd.read_excel(xlsx, 'Sheet1')
```

* Read and Write to SQL Query or Database Table
```python
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')
pd.read_sql("SELECT * FROM my_table;", engine)
pd.read_sql_table('my_table', engine)
pd.read_sql_query("SELECT * FROM my_table;", engine)
# read_sql() is a convenience wrapper around read_sql_table() and read_sql_query()
df.to_sql('myDf', engine)
```

### Asking For Help
```python
help(pd.Series.loc)
```

### Selection - Getting
* getting: Get one element
```python
s['b']
```

* getting: Get subset of a DataFrame
```python
df[1:]
  country Capital   Population
1 India   New Delhi 1303171035
2 Brazil  Brasília  207847528
```

### Selecting, Boolean Indexing & Setting
* By Position: Select single value by row & column
```python
df.iloc[[0],[0]]
# 'Belgium'
df.iat([0],[0])
# 'Belgium'
```

* By Label: Select single value by row & column labels
```python
df.loc[[0],['Country']]
# 'Belgium'
df.at([0],['Country'])
# 'Belgium'
```

* By Label/Position
```python
# Select single row of subset of rows
df.ix[2]
# Country     Brazil 
# Capital     Brasília
# Population  207847528

# Select a single column of subset of columns
df.ix[:,'Capital']
# 0 Brussels
# 1 New delhi
# 2 Brasília

# Select rows and columns
df.ix[1,'Capital']
# 'New Delhi'
```

* Boolean Indexing
```python
# Series s where value is not > 1
s[~(s > 1)]
# s where value is < -1 or > 2
s[(s<-1) | (s>2)]
# Use filter to adjust DataFrame
df[df['Population']>1200000000]
```

* Setting
```python
# Set index a of Series s to 6
s['a'] = 6
```

### Dropping
```python
# Drop values from rows(axis = 0)
s.drop(['a', 'c'])
# Drop values from columns(axis = 1)
df.drop('Country', axis=1)
```

### Sort & Rank
```python
# Sort by labels along an axis
df.sort_index() 
# Sort by the values along an axis
df.sort_values(by='Country')
# Assign ranks to entries
df.rank()
```

### Retrieving Series/DataFrame Information
* Basic information
```python
df.shape # (rows, columns)
df.index # Describe index
df.columns # Describe DataFrame columns
df.info() # Info on DataFrame
df.count() # Number of non-NA values
```

* Summary
```python
df.sum() # Sum of values
df.cumsum() # Cummulative sum of values
df.min()/df.max() # Minimum/maximum values
df.idxmin()/df.idxmax() # Minimum/Maximum index value
df.describe() # Summary statistics
df.mean() # Mean of values
df.median() # Median of values
```

### Applying Functions
```python
f = lambda x: x*2
df.apply(f) # Apply function
df.applymap(f) # Apply function element-wise
```

### Data Alignment
* Internal Data Alignment
```python
# NA values are introduced in the indices that don't overlap:
s3 = pd.Series([7, -2, 3], index=['a', 'c', 'd'])
s + s3
# a 10.0
# b NaN
# c 5.0
# d 7.0
```

* Arithmetic Operations with Fill Methods
```python
# You can also do the internal data alignment yourself with the help of the fill methods:
s.add(s3, fill_value=0)
# a 10.0
# b -5.0
# c 5.0
# d 7.0

s.sub(s3, fill_value=2)
s.div(s3, fill_value=4)
s.mul(s3, fill_value=3)
```



