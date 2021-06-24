# Chapter01-3
# 파이썬 심화
# 클래스 메소드, 인스턴스 메소드, 스테틱 메소드
# class method, instance method, static method

# 기본 인스턴스 메소드
class Student(object):
  '''
  Student Class
  Author: Song
  Date: 2021.06.15
  Description: Class, Static, Instance Method
  '''

  # Class Variable
  tuition = 1.0

  def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):
    self._id = id
    self._first_name = first_name
    self._last_name = last_name
    self._email = email
    self._grade = grade
    self._tuition = tuition
    self._gpa = gpa
  
  # Instance method
  def full_name(self):
    return '{}, {}'.format(self._first_name, self._last_name)

  # Instance Method
  def detail_info(self):
    return 'Student Detail Info : {}, {}, {}, {}, {}, {}'.format(self._id, self.full_name(), self._email, self._grade, self._tuition, self._gpa)

  # Instance Method
  def get_fee(self):
    return 'Before Tuition -> Id : {}, fee : {}'.format(self._id, self._tuition)

  # Instance Method
  def get_fee_calc(self):
    return 'After tuition -> Id : {}, fee : {}'.format(self._id, self._tuition * Student.tuition)

  # Instance Method
  def __str__(self):
    return 'Student Info -> name : {}, grade : {}, email : {}'.format(self.full_name(), self._grade, self._email)
  
student_1 = Student(1, 'Kim', 'Sarang', 'student1@naver.com', '1', 400, 3.5)
student_2 = Student(2, 'Lee', 'Myungho', 'student2@daum.net', '2', 500, 4.3)
