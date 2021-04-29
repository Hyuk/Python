# WORD

* 한글 텍스트도 읽기/쓰기가 가능합니다.
```bash
$ pip install python-docx
```

```python
import docx

# Word 파일을 쉽게 다룰 수 있도록
# Document 객체로 변경합니다.
doc = docx.Document("./python.docx")

# Document 객체는 문서를 구성하고 있는 Paragraph(문단) 객체로 변경해서 저장합니다.
doc.paragraphs # 전체 문단 객체들
doc.paragraphs[4].text # 텍스트 추출하기

# 각각의 Paragraph 객체는 문단을 구성하고 있는 Run 객체로 변경해서 저장합니다.
doc.paragraphs[1].runs
doc.paragraphs[1].runs[0].text
doc.paragraphs[1].runs[3].underline = True

doc.save('python_update.docx')
```