import sqlite3

# Database 조회 (없으면 생성)
conn = sqlite3.connect('D:/hugo/playground/python3/python/playground/python_basic/resource/database.db')

# 커서 바인딩
c = conn.cursor()

# 데이터 삭제 1
c.execute("DELETE FROM users WHERE id= ?", (2,))

# 데이터 삭제 2
c.execute("DELETE FROM users WHERE id= :id", {"id": 5})

# 데이터 삭제 3
c.execute("DELETE FROM users WHERE id= '%s'" % 4)
for user in c.execute("SELECT * FROM users"):
  print(user)
  
# 테이블 데이터 삭제
print("users db deleted : ", conn.execute("DELETE FROM users").rowcount, " rows")
conn.close()

for user in c.execute("SELECT * FROM users"):
  print(user)
conn.close()