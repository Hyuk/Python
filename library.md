# Library

## Pandas
* 파일 입출력시 사용된다

### Jupyter Notebook에서 Pandas Library를 Import하지 못할때
jupyter notebook에서 다음 구문을 실행하면 pandas가 설치된다.
```python
!pip install pandas

# Collecting pandas
#   Downloading https://files.pythonhosted.org/packages/26/fc/d0509d445d2724fbc5f9c9a6fc9ce7da794873469739b6c94afc166ac2a2/pandas-0.23.4-cp37-cp37m-win32.whl (6.8MB)
# Collecting pytz>=2011k (from pandas)
#   Downloading https://files.pythonhosted.org/packages/61/28/1d3920e4d1d50b19bc5d24398a7cd85cc7b9a75a490570d5a30c57622d34/pytz-2018.9-py2.py3-none-any.whl (510kB)
# Collecting numpy>=1.9.0 (from pandas)
#   Downloading https://files.pythonhosted.org/packages/42/5a/eaf3de1cd47a5a6baca41215fba0528ee277259604a50229190abf0a6dd2/numpy-1.15.4-cp37-none-win32.whl (9.9MB)
# Requirement already satisfied: python-dateutil>=2.5.0 in d:\programs\python\python37-32\lib\site-packages (from pandas) (2.7.5)
# Requirement already satisfied: six>=1.5 in d:\programs\python\python37-32\lib\site-packages (from python-dateutil>=2.5.0->pandas) (1.12.0)
# Installing collected packages: pytz, numpy, pandas
# Successfully installed numpy-1.15.4 pandas-0.23.4 pytz-2018.9

```

## 라이브러리 불러오기
```python
import os
from os import listdir
# 현재 폴더의 파일을 열거한다
```
