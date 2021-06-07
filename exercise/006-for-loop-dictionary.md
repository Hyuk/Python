# dictionary for loop

* 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
```python
q1 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for k, v in q1.items():
  if k == "가을":
    print(v)

# 사과

for k in q1:
  if k == "가을":
    print(q1[k])

# 사과
```

* 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
```python
q2 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for k, v in q2.items():
  if v == "사과":
    print(k, v)
    break
else:
  print("사과 없음")
```

