# PDF

* PyPDF2는 윈도우에서 설치 및 실행 가능합니다.
```bash
$ pip install PyPDF2
```

```python
# PDF 파일을 다룰 수 있도록 PyPDF2 라이브러리를 임포트한다.
import PyPDF2

# PDF 파일을 쉽게 다룰 수 있도록
# PdfFileReader 객체로 변경한다.
pdf_fp = open("./python.pdf","rb")
pdf_reader = PyPDF2.PdfFileReader(pdf_fp)

# 전체 페이지 수
pages_count = pdf_reader.numPages

# 특정 페이지 뽑기
pdf_page_0 = pdf_reader.getPage(0)

# 특정 페이지에서 텍스트 추출하기
pdf_page_0.extractText()
```