```python
# Section12-1
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

import sqlite3
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now : ', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)

# sqlite3
print('sqlite3.version : ', sqlite3.version)
print('sqlite3.sqlite_version :', sqlite3.sqlite_version)

# DB 생성 &  Auto Commit(Rollback)

conn = sqlite3.connect('D:/hugo/playground/python3/python/playground/python_basic/resource/database.db', isolation_level=None)

# Cursor
c = conn.cursor()
print('Cursor Type : ', type(c))

# 테이블 생성(Data Type : TEXT, NUMERIC, INTEGER, REAL, BLOB)
# c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

# 데이터 삽입
# c.execute("INSERT INTO users VALUES(1, 'Kim', 'Kim@naver.com', '010-0000-0000', \
#         'Kim.com', ?)",(nowDatetime,))
    
# c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)",(2, 'Park', 'Park@daum.net', '010-1111-1111', 'Park.com', nowDatetime))

# Many 삽입(튜플, 리스트)
userTuple = (
    (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', nowDatetime),
    (4, 'Cho', 'Cho@daum.net', '010-3333-3333', 'Cho.com', nowDatetime),
    (5, 'Yoo', 'Yoo@google.com', '010-4444-4444', 'Yoo.net', nowDatetime)
)

# c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", userTuple)

# 테이블 데이터 삭제

# conn.execute("DELETE FROM users")
# print("users db deleted : ", conn.execute("DELETE FROM users").rowcount)

# 커밋 : isolation_level = None 일 경우 자동 반영(오토 커밋)
# conn.commit()

# 롤백
# conn.rollback()

# 접속 해제
# conn.close()

```

## 테이블 조회, 조건 조회
```python
import sqlite3

# Database 조회 (없으면 생성)
conn = sqlite3.connect('D:/hugo/playground/python3/python/playground/python_basic/resource/database.db')

# 커서 바인딩
c = conn.cursor()

# 데이터 조회(전체)
c.execute("SELECT * FROM users")

# 커서 위치가 변경
# 1개 로우 선택
print('One -> \n', c.fetchone()) # cursor가 위치한 첫번째 데이터를 가져온다.

# 지정 로우 선택
print('Three -> \n', c.fetchmany(size=3)) # cursor가 위치한 2, 3, 4 데이터를 가져온다.

# 전체 로우 선택
print('All -> \n', c.fetchall()) # cursor가 위치한 나머지 데이터를 가져온다.

# 순회 방법 1
rows = c.fetchall()
for row in rows:
  print('retrieve1 > ', row)

# 순회 방법 2
for row in c.fetchall():
  print('retrieve2 > ', row)

# 순회 방법 3
for row in c.execute("SELECT * FROM users ORDER BY id desc")
  print('retrieve3 > ', row)
```

## 조건 검색 where
```python
# 조건 검색 방법 1
param1 = (3,)
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1', c.fetchone())
# param1 (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', '2021-06-11 08:47:31')
print('param1', c.fetchall()) # 나머지 데이터 없음

# 조건 검색 방법 2
param2 = 4
c.execute('SELECT * FROM users WHERE id="%s"' % param2)
print('param2', c.fetchone()) 
# param2 (4, 'Cho', 'Cho@daum.net', '010-3333-3333', 'Cho.com', '2021-06-11 08:47:31')
print('param2', c.fetchall())

# 조건 검색 방법 3
c.execute('SELECT * FROM users WHERE id=:Id', {"Id": 5})
print('param3', c.fetchone()) 
# param3 (5, 'Yoo', 'Yoo@google.com', '010-4444-4444', 'Yoo.net', '2021-06-11 08:47:31')
print('param3', c.fetchall())

# 조건 검색 방법 4
param4 = (3,5)
c.execute('SELECT * FROM users WHERE id IN(?,?)', param4) # IN 합집합
print('param4', c.fetchall())
# param4 [(3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', '2021-06-11 08:47:31'), (5, 'Yoo', 'Yoo@google.com',  '010-4444-4444', 'Yoo.net', '2021-06-11 08:47:31')]

# 조건 검색 방법 5
c.execute("SELECT * FROM users WHERE id IN('%d','%d')" % (3,4)) # IN 합집합
print('param5', c.fetchall())

# 조건 검색 방법 6
c.execute("SELECT * FROM users WHERE id=:id1 OR id=:id2", {"id1": 2, "id2": 5}) # IN 합집합
print('param6', c.fetchall())
# param6 [(2, 'Park', 'Park@daum.net', '010-1111-1111', 'Park.com', '2021-06-11 08:47:31'), (5, 'Yoo', 'Yoo@google.com', '010-4444-4444', 'Yoo.net', '2021-06-11 08:47:31')]

# Dump 출력
with conn:
  with open('D:/hugo/playground/python3/python/playground/python_basic/resource/dump.sql','w') as f:
    for line in conn.iterdump():
      f.write('%s\n' % line)
    print('Dump Print Complete')

# dump.sql
# BEGIN TRANSACTION;
# CREATE TABLE users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text);
# INSERT INTO "users" VALUES(1,'Kim','Kim@naver.com','010-0000-0000','Kim.com','2021-06-11 08:47:31');
# INSERT INTO "users" VALUES(2,'Park','Park@daum.net','010-1111-1111','Park.com','2021-06-11 08:47:31');
# INSERT INTO "users" VALUES(3,'Lee','Lee@naver.com','010-2222-2222','Lee.com','2021-06-11 08:47:31');
# INSERT INTO "users" VALUES(4,'Cho','Cho@daum.net','010-3333-3333','Cho.com','2021-06-11 08:47:31');
# INSERT INTO "users" VALUES(5,'Yoo','Yoo@google.com','010-4444-4444','Yoo.net','2021-06-11 08:47:31');
# COMMIT;
```

## 테이블 수정, 삭제
```python
import sqlite3

# DB생성(파일)
conn = sqlite3.connect('D:/hugo/playground/python3/python/playground/python_basic/resource/database.db')

# Cursor 연결
c = conn.cursor()

# 데이터 수정 1
c.execute("UPDATE users SET username = ? WHERE id = ?", ('niceman', 2))
conn.commit()

# 데이터 수정 2
c.execute("UPDATE users SET username = :name WHERE id = :id", {"name": 'goodman', "id": 5})
conn.commit()

# 데이터 수정 3
c.execute("UPDATE users SET username = '%s' WHERE id = '%s'" % ('badboy', 3))
conn.commit()

# 중간 데이터 확인 1
for user in c.execute("SELECT * FROM users"):
  print(user)

# 데이터 삭제 1
c.execute("DELETE FROM users WHERE id= ?", (2,))

# 데이터 삭제 2
c.execute("DELETE FROM users WHERE id= :id", {"id": 5})

# 데이터 삭제 3
c.execute("DELETE FROM users WHERE id= '%s'" % 4)

# 테이블 데이터 삭제
print("users db deleted : ", conn.execute("DELETE FROM users").rowcount, " rows")
```