# File I/O - XSL, XLSX Format

* openpyxl, xlsxwriter, xlrd, xlwt, xlutils
* pandas 를 주로 사용
* 설치하는 방법
```bash
$ pip install xlrd
$ pip install openpyxl
$ pip install pandas
```

```python
import pandas as pd

# sheetname='시트명' 또는 숫자, header=3, skiprow=숫자
xlsx = pd.read_excel('./resource/sample.xlsx')
# 상위 데이터 확인
print(xlsx.head()) # 첫 번째부터 5개 까지만 보여준다.
print()
print(xlsx.tail()) # 마지막 5개를 보여준다.
# 데이터 확인
print(xlsx.shape) # 행, 열
# 엑셀 or CSV 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)
```


